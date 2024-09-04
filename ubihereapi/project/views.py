from rest_framework import generics, permissions
from .serializers import ProjectSerializer
from .models import Project
from rest_framework.parsers import MultiPartParser, FormParser


# List and create 

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # If not authenticate we can only see the projects

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # To parse incoming form data

    parser_classes = (MultiPartParser, FormParser)

class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # To parse incoming form data

    parser_classes = (MultiPartParser, FormParser)
    