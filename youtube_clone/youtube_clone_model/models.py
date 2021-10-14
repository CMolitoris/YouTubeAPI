from django.db import models

# Create your models here.
class Comment(models.Model):
    username = models.CharField(max_length=50)
    body = models.CharField(max_length=150)
    videoId = models.CharField(max_length=150)
    likes = models.IntegerField(default=0,null=False)
    dislikes = models.IntegerField(default=0,null=False) 

class Reply(models.Model):
    body = models.CharField(max_length=150)  
    commentId = models.ForeignKey(Comment, on_delete=models.CASCADE)  