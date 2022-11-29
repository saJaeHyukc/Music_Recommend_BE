from django.db import models

from users.models import User

class Song(models.Model):
    year = models.CharField(max_length=70, blank=True)
    rank = models.CharField(max_length=70, blank=True)
    title = models.CharField(max_length=70, blank=True)
    genre = models.CharField(max_length=70, blank=True)
    singer = models.CharField(max_length=70, blank=True)
    type = models.CharField(max_length=70, blank=True)
    lyrics = models.TextField(blank=True)
    likes = models.IntegerField(blank=True)
    image = models.TextField(blank=True)
    genre_no = models.IntegerField(blank=True)
    youtube_url = models.TextField(blank=True)
    
    song_likes = models.ManyToManyField(User, related_name="like_song",blank=True)
    
    class Meta: 
        db_table = 'song'
        ordering = ['id']

    def __str__(self):
        return str(self.title) 


class Voice(models.Model):
    recode = models.FileField(upload_to="voice_record")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    voice_likes = models.ManyToManyField(User, related_name="like_voice", blank=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="voices")
    class Meta:
        db_table = 'voice'
        ordering = ['-created_at']

class Comment(models.Model):
    content= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return str(self.content)
    
    class Meta:
        db_table = 'comment'
        ordering = ['-created_at']
