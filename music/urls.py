from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    #/music/
    path('',views.indexView.as_view(),name='index'),
    #/register
    path('register/',views.UserFormView.as_view(),name='register'),
    #/music/1/
    path('<int:pk>/',views.detailView.as_view(),name='detail'),
    #/music/add/
    path('add/',views.addView.as_view(),name='detail_add'),
    #/music/1/delete/
    path('<int:pk>/delete/',views.deleteView.as_view(),name='detail_delete'),
]
