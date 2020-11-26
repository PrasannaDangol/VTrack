from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.


class Map(models.Model):
    user = models.OneToOneField(User, default='', on_delete=models.CASCADE)
    location = models.CharField(default='', max_length=60)

    def __str__(self):
        return f'{self.user.username}'

class Vehicle(models.Model):
    vehicle_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    licensenumber = models.CharField(default='', max_length=60)
    location = models.CharField(default='', max_length=60)
    Time = models.TimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f'{self.licensenumber}'

class MissingVehicle(models.Model):
    missingVehicle_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_id = models.IntegerField(default='')

    def __str__(self):
        return f'{self.profile_id}'


