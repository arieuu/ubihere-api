from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectListCreateAPI.as_view())
]
