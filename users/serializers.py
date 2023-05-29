from rest_framework import serializers
from django.contrib.auth.models import User, Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name")


class UserSerializer(serializers.ModelSerializer):
    # groups = GroupSerializer(many=True, read_only=True, source="group_set")

    class Meta:
        model = User
        fields = "__all__"
