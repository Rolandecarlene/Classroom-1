from tkinter.constants import UNITS
from django.db import models

#Create your models here.

class Property(models.Model):
    PropertyType = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('commercial', 'Commercial'),
    ]
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()
    property_type = models.CharField(max_length=100, choices=PropertyType)
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    bedrooms = models.IntegerField()
    rent = models.IntegerField()
    is_available = models.BooleanField()
    bathrooms = models.IntegerField()
    unit_amount = models.IntegerField()

    def __str__(self):
        return f"{self.property} - {self.unit_amount}"


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    units = models.ForeignKey(Unit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.IntegerField()

    def __str__(self):
        return f"{self.tenant} - {self.units}"




















