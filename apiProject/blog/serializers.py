from rest_framework import serializers
from .models import Category, Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        model = Comment

    def get_creator(self, obj):
        return obj.creator.username


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category


class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    dislike_count = serializers.SerializerMethodField()
    creator = serializers.SerializerMethodField()
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True
    )
    category_name = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        fields = [
            "id",
            "title",
            "content",
            "creator",
            "like_count",
            "dislike_count",
            "category_name",
            "category",
            "comments",
        ]
        read_only_fields = [
            "id",
            "creator",
            "comments",
            "category_name",
        ]
        model = Post

    def get_like_count(self, obj):
        return obj.likes.count()

    def get_dislike_count(self, obj):
        return obj.dislikes.count()

    def get_creator(self, obj):
        return obj.creator.username

    def get_category_name(self, obj):
        return obj.category.name
