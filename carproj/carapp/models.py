from django.db import models
from django.contrib import admin

class Car_Inventory(models.Model):
    Plate_no=models.IntegerField(primary_key=True)
    Car_type=models.CharField(max_length=20)
    Car_brand=models.CharField(max_length=20)
    Manufacturing_date=models.DateField()
    Car_color=models.CharField(max_length=20)
    Price=models.IntegerField()
    Mileage=models.CharField(max_length=20)


class Car_InventoryAdmin(admin.ModelAdmin):
    list_display=['Plate_no', 'Car_type', 'Car_brand', 'Manufacturing_date', 'Car_color', 'Price', 'Mileage']

# Create your models here.
