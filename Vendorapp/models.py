from django.db import models
from adminapp.models import CityModel,CuisineModel
class VendorRegistrationModel(models.Model):
    v_id=models.AutoField(primary_key=True)
    v_stall_name=models.CharField(max_length=200)
    v_contact1=models.IntegerField(unique=True)
    v_contact2=models.IntegerField(unique=True)
    v_cuisine_type=models.ForeignKey(CuisineModel,on_delete=models.CASCADE)
    v_stall_photo=models.ImageField(upload_to="vendor_images/")
    v_stall_address=models.TextField()
    v_stall_city=models.ForeignKey(CityModel,on_delete=models.CASCADE)
    v_password=models.CharField(max_length=10)
    v_otp=models.IntegerField()

class FoodTypeModel(models.Model):
    food_id=models.AutoField(primary_key=True)
    food_type=models.CharField(max_length=200)
    vendor_id=models.ForeignKey(CuisineModel,on_delete=models.CASCADE)
    food_photo=models.ForeignKey(VendorRegistrationModel,on_delete=models.CASCADE)
    status=models.CharField(max_length=3000)
class FoodItemsModel(models.Model):
    item_id=models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=500)
    item_type=models.ForeignKey(FoodTypeModel,on_delete=models.CASCADE)
    item_price=models.FloatField()
    item_pic=models.ImageField(upload_to="food_images/")
