from django.urls import path, include
from .views import PostList, LikePostView, DislikePostView, CommentPostView, CreatePost

urlpatterns = [
    path("posts", PostList.as_view(), name="posts"),
    path("create-post", CreatePost.as_view(), name="create-post"),
    path("like/<int:pk>", LikePostView.as_view(), name="like-post"),
    path("dislike/<int:pk>", DislikePostView.as_view(), name="dislike-post"),
    path("comment/<int:pk>", CommentPostView.as_view(), name="create-comment"),
]
