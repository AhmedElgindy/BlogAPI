from rest_framework import generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, status
from rest_framework.response import Response


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreatePost(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


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
