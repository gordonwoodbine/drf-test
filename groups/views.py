from rest_framework import viewsets
from django.contrib.auth.models import Group, User
from .serializers import GroupSerializer


# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.prefetch_related("user_set")
    serializer_class = GroupSerializer
