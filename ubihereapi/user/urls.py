from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserListCreateAPIView.as_view())
]


    
