from .models import Blog, Category, Comment
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("title", "slug", "description")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "category_title"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "comment"
