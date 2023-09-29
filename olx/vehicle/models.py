from django.db import models

# Create your models here.

class Vehicles(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year=models.IntegerField()
    vehicle_number = models.CharField(max_length=255)
    owner = models.CharField(max_length=200)
    mileage = models.IntegerField()
    description = models.TextField(blank=True)
    image=models.ImageField(upload_to="images",null=True)


    def __str__(self):
        return self.name