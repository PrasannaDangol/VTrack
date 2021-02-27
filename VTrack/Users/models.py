from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)# one to one with user and if user is deleted profile picture is also deleted but not vice versa
    phonenumber = models.CharField(max_length=12)
    licensenumber = models.CharField(default='', max_length=60)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.CharField(default='', max_length=60)


    def __str__(self):
        return f'{self.user.username}'


