from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Album
# Create your views here.

# def index(request):
#     all_albums=Album.objects.all()
#     # html = ''
#     # for album in all_albums:
#     #     url=''+str(album.id)+'/'
#     #     html += '<a href="'+url+'">'+album.album_title+'</a><br>'
#     return render(request,"music/index.html",{'all_albums':all_albums})
#
# def detail(request,album_id):
#     # try:
#     #     album = Album.objects.get(pk=album_id)#获取pk为1所对应的objects
#     # except Album.DoesNotExist:#超出应有pk值则报错
#     #     raise Http404('wrong input!!')
#     album = get_object_or_404(Album,pk=album_id)#查询对应pk的Album对象是否存在，不存在就返回个404
#     return render(request,'music/detail.html',{'album':album})
#
# def favourate(request,album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except (KeyError,Song.DoesNotExist):
#         return render(request,'music/detail,html',{
#             'album':album,
#             'errot_message': "you need to choose one",
#         })
#     else:
#         selected_song.is_favourate = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album': album})

from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect  #when login function
from django.contrib.auth import authenticate,login   #when login function
from django.views.generic import View   #when login function
from .models import Album
from .form import UserForm   #when login function

class indexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class detailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class addView(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class deleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/regestration_form.html'

    #display blan form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})
    #process from data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():#save in database
            user = form.save(commit=False)

            #cleaned normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username,password=password)

            if user is not None:#if login successfully,redirect to index
                if user.is_active:
                    login(request,user)
                    return redirect('music:index')

        return render(request,self.template_name,{'form':form})