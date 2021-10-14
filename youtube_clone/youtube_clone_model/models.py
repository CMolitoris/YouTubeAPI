from django.db import models

# Create your models here.
class Comment(models.Model):
    username = models.TextField(max_length=35,blank=True,null=True)
    body = models.TextField(max_length=250)
    videoId = models.TextField(max_length=11)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0) 

class Reply(models.Model):
    body = models.TextField(max_length=250)  
    commentId = models.ForeignKey(Comment, on_delete=models.CASCADE)  