from django.urls import path, include
from .views import (
    PostList,
    LikePostView,
    DislikePostView,
    CommentPostView,
    CreatePost,
    CategoryList,
    posts_by_category,
)

urlpatterns = [
    path("posts", PostList.as_view(), name="posts"),
    path("categories", CategoryList.as_view(), name="categorys"),
    path("create-post", CreatePost.as_view(), name="create-post"),
    path("like/<int:pk>", LikePostView.as_view(), name="like-post"),
    path("dislike/<int:pk>", DislikePostView.as_view(), name="dislike-post"),
    path("comment/<int:pk>", CommentPostView.as_view(), name="create-comment"),
    path(
        "category/<int:category_id>/posts",
        posts_by_category,
        name="posts-by-category",
    ),
]
