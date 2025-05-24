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
    
 

class Category(models.Model):
    CategoryID=models.IntegerField(primary_key=True)
    CategoryName=models.CharField(max_length=50)
    CategoryDescription=models.CharField(max_length=255)

  
class Products(models.Model):
    ProductID=models.CharField(max_length=10,primary_key=True)
    ProductName=models.CharField(max_length=50)
    ProductDesc=models.CharField(max_length=255)
    Price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField
    Imageurl=models.ImageField(upload_to='static/')
    CategoryID=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    Added=models.DateTimeField(default=datetime.now)

class Cart(models.Model):
    CartID=models.CharField(max_length=10,primary_key=True)
    UserID=models.ForeignKey(Users,on_delete=models.SET_NULL,null=True,blank=True)
    ProductID=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,blank=True)
    Quantity=models.IntegerField
    Added=models.DateTimeField(default=datetime.now)

  
class Invoice(models.Model):
    DocheaderNo=models.CharField(max_length=20,primary_key=True)
    UserID=models.ForeignKey(Users,on_delete=models.SET_NULL,null=True,blank=True)
    Discount=models.DecimalField(max_digits=10,decimal_places=2)
    Tax=models.DecimalField(max_digits=10,decimal_places=2)
    Beforetax=models.DecimalField(max_digits=10,decimal_places=2)
    Aftertax=models.DecimalField(max_digits=10,decimal_places=2)
    Paymentstatus=models.CharField(max_length=20,default='Unpaid')
    BillingAddress=models.CharField(max_length=255)



class InvoiceDetails(models.Model):
    DocheaderNo=models.CharField(max_length=20,primary_key=True)
    UserID=models.ForeignKey(Users,on_delete=models.SET_NULL,null=True,blank=True)
    InvNo=models.ForeignKey(Invoice,on_delete=models.SET_NULL,null=True,blank=True)
    ProductID=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,blank=True)
    Tax=models.DecimalField(max_digits=10,decimal_places=2)
    Quantity=models.IntegerField
    Price=models.DecimalField(max_digits=10,decimal_places=2)
    GST=models.CharField(max_length=30)


class Payments(models.Model):
    DocNo=models.IntegerField(primary_key=True)
    InvoiceNO=models.ForeignKey(Invoice,on_delete=models.SET_NULL,null=True,blank=True)
    PaymentMethod=models.CharField(max_length=4)
    Amount=models.DecimalField(max_digits=10,decimal_places=2)
    PayementDate=models.DateTimeField(default=datetime.now)
    PaymentStatus=models.CharField(max_length=6)


class Coupouns(models.Model):
    ID=models.IntegerField(primary_key=True)
    Code=models.CharField(max_length=20,unique=True)
    method=models.CharField(max_length=2,default='01')
    DiscountPercent=models.CharField(max_length=2,default='01')
    ValidFrom=models.DateTimeField(default=datetime.now)
    validTill=models.DateField
    ISActive=models.BooleanField(default=1)

  

class Customer(models.Model):
    ID=models.CharField(max_length=10,primary_key=True)
    UserID=models.IntegerField
    Addressline1=models.CharField(max_length=255)
    Addressline2=models.CharField(max_length=255,null=True)
    CustomerState=models.CharField(max_length=50)
    Postalcode=models.CharField(max_length=20)
    created=models.DateTimeField(default=datetime.now)
    GSt=models.CharField(max_length=50)



