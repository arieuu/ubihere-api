from rest_framework import generics, permissions
from .serializers import ProjectSerializer
from .models import Project


# List and create 

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # If not authenticate we can only see the projects

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    