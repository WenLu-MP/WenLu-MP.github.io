from django.db import models
from django.urls import reverse
# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.artist+'-'+self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=20)
    song_title = models.CharField(max_length=250)
    is_favourate = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title