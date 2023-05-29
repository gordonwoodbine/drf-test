from rest_framework import serializers
from django.contrib.auth.models import Group, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True, source="user_set")

    class Meta:
        model = Group
        fields = "__all__"
