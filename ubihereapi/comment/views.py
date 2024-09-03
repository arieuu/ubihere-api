from django.shortcuts import render
from rest_framework import generics
from .serializers import CommentSerializer
from .models import Comment


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer