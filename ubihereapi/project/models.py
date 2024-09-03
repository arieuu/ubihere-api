from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255, null=False)
    about = models.TextField(blank=False, null=False)
    image = models.CharField(max_length=255, null=True)
    owner_email = models.EmailField(max_length=255, null=False)
    total_ratings = models.IntegerField(default=0)
    number_of_responses = models.IntegerField(default=0)
    calculated_rating = models.IntegerField(default=0, null=True)

    @property
    def calculate_rating(self):
        pass
