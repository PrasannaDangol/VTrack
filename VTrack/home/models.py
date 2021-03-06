from django.db import models
import uuid

class MissingVehicle(models.Model):
    missingVehicle_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    licensenumber = models.CharField(default='', max_length=60)
    email = models.CharField(default='', max_length=12)
    mes = models.CharField(default='', max_length=500)
    class Meta:
        db_table = "missingvehicle"

    # def __str__(self):
    #     return f'{self.missingVehicle_id}'