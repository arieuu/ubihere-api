from rest_framework import generics
from .serializers import ProjectSerializer
from .models import Project


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer