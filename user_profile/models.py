from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
import os


class CustomUser(AbstractUser):
    """
    CustomUser extends/builds upon the base User
    model so that custom fields can be added
    """
    location = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    picture = CloudinaryField(
        'image',
        default='default_profile',
        blank=True
    )

    def __str__(self):
        return self.username
