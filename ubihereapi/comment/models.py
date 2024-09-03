from django.db import models

# Create your models here.


class Comment(models.Model):
    commenter_name = models.CharField(max_length=255, null=False)
    comment_owner_email = models.EmailField(max_length=255, null=False)
    content = models.TextField(null=False)
    project_id = models.IntegerField(null=False)