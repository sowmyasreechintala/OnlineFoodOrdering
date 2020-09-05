from django.db import models
from  adminapp.models import CityModel
from  Vendorapp.models import FoodItemsModel
class CustomerRegistrationModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    contactno=models.IntegerField(unique=True)
    address=models.TextField(max_length=100)
    city=models.ForeignKey(CityModel,on_delete=models.CASCADE)
    password=models.CharField(max_length=20)
    otp=models.IntegerField()

class OrderModel(models.Model):
    id = models.AutoField(primary_key=True)
    items=models.ManyToManyField(FoodItemsModel)
    qty=models.IntegerField()
    total=models.FloatField()
    status=models.CharField(max_length=20)
    date=models.DateField(auto_now_add=True)
    address=models.TextField()
