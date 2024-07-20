from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=100)
    user_profile_image = models.ImageField(upload_to='profile')
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()
    


# Another Method to do without creating manager.py | Just write it and createsuperuser 

# class CustomUser(AbstractUser):
#     name = models.CharField(max_length=200, null=True)
#     email = models.EmailField(unique=True)
#     bio = models.TextField(null=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []