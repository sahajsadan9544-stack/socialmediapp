from rest_framework import serializers
from sm_app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id", "username", "password", "email", "first_name", "last_name"]
        read_only_fields=["id"]

    def create(self, validated_data):   #passwrd hashing
        return CustomUser.objects.create_user(**validated_data)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=["id", "title", "image", "description", "created_at", "owner"]
        read_only_fields=["created_at", "owner"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=["id", "comment", "added_at", "owner", "post_obj"]
        read_only_fields=["added_at"]

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields="__all__"
