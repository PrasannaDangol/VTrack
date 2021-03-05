from django.contrib import admin
from .models import Map
from .models import Vehicle
from .models import MissingVehicle

# Register your models here.
admin.site.register(Map)
admin.site.register(Vehicle)
admin.site.register(MissingVehicle)