from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectListCreateAPIView.as_view()),
    path("<int:pk>", views.ProjectRetrieveUpdateDestroyAPIView.as_view())
]
