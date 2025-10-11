# Ex02 Django ORM Web Application
# Date:26.09.2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
```
admin.py

from django.contrib import admin
from .models import Car_Inventory, Car_InventoryAdmin
admin.site.register(Car_Inventory, Car_InventoryAdmin)

models.py

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
```
# OUTPUT!
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1320f304-19b1-4aa8-a58b-0de7b1b7617f" />



# RESULT
Thus the program for creating a database using ORM hass been executed successfully
