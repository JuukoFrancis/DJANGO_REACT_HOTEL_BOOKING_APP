from django.db import models

# Create your models here.
class Room(models.Model):
    ROOM_TYPES = [
        ('suite','Suite'),
        ('standard','Standard Room'),
        ('deluxe','Deluxe Room')
                  ]
    
    CURRENCY_TYPES = [
        ('USD','USD'),
        ('USD','EUR'),
        ('UGX','UGX')
                  ]
    
    name = models.CharField(max_length=100, blank=True, default="")
    type = models.CharField(max_length=100,  choices=ROOM_TYPES)
    pricePerNIght = models.IntegerField(default=150)
    currency = models.CharField(default="UGX", max_length=10, choices=CURRENCY_TYPES)
    maxOccupancy = models.IntegerField(default=1)
    description = models.TextField(max_length=1)
    # 07:40

