from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime
from django.utils.timezone import utc

# Create your models here.



class Map(models.Model):
    user = models.OneToOneField(User, default='', on_delete=models.CASCADE)
    location = models.CharField(default='', max_length=60)

    def __str__(self):
        return f'{self.user.username}'

class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    licensenumber = models.CharField(default='', max_length=60)
    location = models.CharField(default='', max_length=60)
    Time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.licensenumber}'

class MissingVehicle(models.Model):
    missingVehicle_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_id = models.IntegerField(default='')

    def __str__(self):
        return f'{self.profile_id}'


