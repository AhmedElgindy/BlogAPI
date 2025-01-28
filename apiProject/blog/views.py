from rest_framework import generics
from .models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreatePost(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the creator to the authenticated user
        serializer.save(creator=self.request.user)


# class PostCreate(generics.)
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user
        if post.likes.filter(id=user.id):
            post.likes.remove(user)
            return Response({"status": "unliked"})
        post.likes.add(user)
        return Response({"status": "liked"}, status=status.HTTP_200_OK)


class DislikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user
        if post.dislikes.filter(id=user.id):
            post.dislikes.remove(user)
            return Response({"status": "undisliked"})
        post.dislikes.add(user)
        return Response({"status": "disliked"}, status=status.HTTP_200_OK)


class CommentPostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        content = request.data.get("content", None)
        if not content:
            return Response(
                {"error": "Content Required"}, status=status.HTTP_400_BAD_REQUEST
            )

        comment = Comment.objects.create(post=post, creator=user, content=content)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def posts_by_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)

        posts = Post.objects.filter(category=category)
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(result_page, many=True)

        return paginator.get_paginated_response(
            {"category": category.name, "posts": serializer.data}
        )

    except:
        return Response(
            {"error": "Category Not Found "}, status=status.HTTP_400_NOT_FOUND
        )
