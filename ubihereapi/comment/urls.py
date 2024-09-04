from django.urls import path
from . import views

urlpatterns = [
    path("", views.CommentListCreateAPIView.as_view()),
    path("<int:pk>", views.CommentRetrieveUpdateDestroyAPIView.as_view())
]
