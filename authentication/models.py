from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    fav_color = models.CharField(blank=True, max_length=120)
    email = models.EmailField(unique=True, error_messages={'unique':"Email already exists"})