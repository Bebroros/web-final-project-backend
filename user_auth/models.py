from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    date = models.DateField(default='1111-1-1')
