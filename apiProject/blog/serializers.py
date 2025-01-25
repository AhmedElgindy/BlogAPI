from rest_framework import serializers
from .models import Category, Post, Comment


class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    dislike_count = serializers.SerializerMethodField()
    creator = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        fields = [
            "id",
            "title",
            "content",
            "creator",
            "like_count",
            "dislike_count",
            "category",
            "comments",
        ]
        model = Post

    def get_like_count(self, obj):
        return obj.likes.count()

    def get_dislike_count(self, obj):
        return obj.dislikes.count()

    def get_creator(self, obj):
        return obj.creator.username

    def get_category(self, obj):
        return obj.category.name


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Comment
