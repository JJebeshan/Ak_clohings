from django.db import models
from datetime import datetime
# Create your models here.
class Users(models.Model):
    id=models.IntegerField(primary_key=True)
    Firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=50 )
    password=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    role=models.CharField(max_length=10, null=True)
    action=models.CharField(max_length=4, null=True)
    Created=models.DateTimeField (null=True)
    
    class meta:
        managed=False
        db_table='Users'

class Category(models.Model):
    CategoryID=models.IntegerField(primary_key=True)
    CategoryName=models.CharField(max_length=50)
    CategoryDescription=models.CharField(max_length=255)

    class meta:
        managed=False
        db_table='Category'

class Products(models.Model):
    ProductID=models.CharField(max_length=10,primary_key=True)
    ProductName=models.CharField(max_length=50)
    ProductDesc=models.CharField(max_length=255)
    Price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    Imageurl=models.ImageField(upload_to='static/')
    CategoryID=models.ForeignKey(Category,on_delete=models.SET_NULL=True,blank=True)
    Added=models.DateTimeField(default=datetime.now)

    class meta:
        managed=False
        db_table='Products'
