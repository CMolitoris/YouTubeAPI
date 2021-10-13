from django.urls import path
from . import views

urlpatterns = [
    path('comments/',views.CommentList.as_view()),
    path('comments/<int:pk>/',views.CommentDetail.as_view()),
    path('comments/<int:pk>/<str:field>/',views.CommentDetail.as_view()),
    path('replies/',views.ReplyList.as_view()),
    path('replies/<int:pk>/',views.ReplyDetail.as_view()),
    path('replies/<int:pk>/<str:field>/',views.ReplyDetail.as_view())
]