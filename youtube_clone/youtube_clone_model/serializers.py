from rest_framework import serializers
from .models import Comment, Reply

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            
            'id',
            'username',
            'body',
            'videoId'
            
            
        ]

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = [
            'id',
            'body',
            'commentId'
            
        ]        