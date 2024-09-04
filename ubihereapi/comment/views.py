from rest_framework import generics, permissions
from .serializers import CommentSerializer
from .models import Comment

# List and create

class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Retrieve update and delete

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]