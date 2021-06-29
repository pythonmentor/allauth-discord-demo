from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Represent a user of the application."""
