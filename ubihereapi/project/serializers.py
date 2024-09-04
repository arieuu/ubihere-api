from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=False)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "about",
            "image",
            "owner_email",
            "total_ratings",
            "calculated_rating",
            "number_of_responses"
        ]