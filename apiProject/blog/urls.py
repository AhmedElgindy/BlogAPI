from django.urls import path, include
from .views import PostList, LikePostView, DislikePostView

urlpatterns = [
    path("posts", PostList.as_view(), name="posts"),
    path("like/<int:pk>", LikePostView.as_view(), name="like-post"),
    path("dislike/<int:pk>", DislikePostView.as_view(), name="dislike-post"),
]
