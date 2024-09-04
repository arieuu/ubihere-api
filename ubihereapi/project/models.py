from django.db import models

# Explicitly setting up upload and filename

def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255, null=False)
    about = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    owner_email = models.EmailField(max_length=255, null=False)
    total_ratings = models.IntegerField(default=0)
    number_of_responses = models.IntegerField(default=0)
    calculated_rating = models.IntegerField(default=0, null=True)

    @property
    def calculate_rating(self):
        pass
