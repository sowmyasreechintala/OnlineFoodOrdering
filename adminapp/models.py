from django.db import models

class StateModel(models.Model):
    state_id=models.AutoField(primary_key=True)
    state_name=models.CharField(max_length=200,unique=True)
    state_photo=models.ImageField(upload_to="state_images/")

class CityModel(models.Model):
    city_id=models.AutoField(primary_key=True)
    city_name=models.CharField(max_length=200,unique=True)
    city_photo=models.ImageField(upload_to="city_images/")
    city_state=models.ForeignKey('StateModel',on_delete=models.CASCADE)

class CuisineModel(models.Model):
    cuisine_id=models.AutoField(primary_key=True)
    cuisine_name=models.CharField(max_length=200,unique=True)
    cuisine_photo=models.ImageField(upload_to="cuisine_images/")

class AdminLoginModel(models.Model):
    username=models.CharField(primary_key=True,max_length=50)
    password=models.CharField(max_length=50)
    otp=models.IntegerField(default=1234)