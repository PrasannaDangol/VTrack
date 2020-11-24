from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Map(models.Model):
    user = models.OneToOneField(User,default='', on_delete=models.CASCADE)
    location = models.CharField(default='', max_length=60)

    def __str__(self):
        return f'{self.user.username}'


