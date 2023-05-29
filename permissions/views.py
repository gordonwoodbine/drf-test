from rest_framework import viewsets
from django.contrib.auth.models import Permission
from .serializers import PermissionSerializer


# Create your views here.
class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
