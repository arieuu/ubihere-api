from django.db import models
from django.contrib.auth import models as auth_models


class UserManager(auth_models.BaseUserManager):

    def create_user(self, name: str, email: str, password: str = None, is_staff=False, is_superuser=False) -> "User":

        if not name:
            raise ValueError("Name is required")

        if not email:
            raise ValueError("Email is required")

        # Set up the values

        user = self.model(email=self.normalize_email(email))
        user.name = name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser

        user.save()

        return user

    
    def create_superuser(self, name: str, email: str, password: str) -> "User":
        user = self.create_user(name=name,
                                email=email, 
                                password=password,
                                is_staff=True,
                                is_superuser=True)

        user.save()
        return user

class User(auth_models.AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    objects = UserManager()
  
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]