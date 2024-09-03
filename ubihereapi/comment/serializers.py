from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            "id",
            "commenter_name",
            "comment_owner_email",
            "content",
            "project_id"
        ]