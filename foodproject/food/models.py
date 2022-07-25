from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class fooddetails(models.Model):
    Nameofdonor=models.CharField("Enter name",max_length=100)
    Itemname=models.CharField("Enter food item name",max_length=100)
    Itype=models.CharField("enter Item type",max_length=100)
    Hlevel=models.IntegerField(default=0)
    Location=models.TextField()
    Email=models.EmailField(default="null")
    Date=models.IntegerField(default=0)
    Fexpiry=models.IntegerField(default=0)
    Mobileno=models.IntegerField(default=0)
