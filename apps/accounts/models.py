from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email: models.EmailField = models.EmailField(unique=True)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    USERNAME_FIELD: str = "email" # use email for login
    REQUIRED_FIELDS: list[str] = [
        "username"
    ]

    def __str__(self):
        return f"EMAIL({self.email}); USERNAME({self.username})"


class Account(models.Model):
    pass


class Plan(models.Model):
    pass