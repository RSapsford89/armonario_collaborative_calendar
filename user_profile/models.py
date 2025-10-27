from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from PIL import Image
# Create your models here.


class CustomUser(AbstractUser):
    """
    CustomUser extends/builds upon the base User
    model so that custom fields can be added
    """
    #Custom user fields follow here and should not
    #be the same as existing User.<object> fields
    #should also be blank=True to not break auth

    location = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField( max_length=50, blank=True)
    date_joined = models.DateTimeField( auto_now_add=True)
    picture = CloudinaryField('image', default='profile/default_profile.webp', blank=True)
    
    def __str__(self):
        return self.username
    

