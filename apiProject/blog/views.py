from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, status
from rest_framework.response import Response


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


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
