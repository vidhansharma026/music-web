from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=20)
    singers = models.CharField(max_length=255)
    image = models.ImageField(upload_to='song_img')
    audio_file = models.FileField(upload_to='music')
    duration = models.CharField(max_length=10)
    
    def __str__(self) :
        return str(self.title)
    


