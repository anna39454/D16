from django.urls import path
from .views import *


urlpatterns = [
   path('confirm/', ConfirmUser.as_view(), name='confirm_user'),
   path('profile', ProfileView.as_view(), name= 'profile'),
   path('post/', PostList.as_view()),
   path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('post/create/', PostCreate.as_view(), name='post_create'),
   path('post/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('comment/create/', CommentCreate.as_view(), name='comment'),
   path('comment/<int:pk>/detail', CommentDetail.as_view()),
   path('comment/<int:pk>/edit/', CommentUpdate.as_view(), name='comment_update'),
   path('comment/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),
]