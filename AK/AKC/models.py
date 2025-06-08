from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Permission,Group
from django.db import models
from django.utils import timezone

PAYMENT_STATUS_CHOICES = [
    ('Unpaid', 'Unpaid'),
    ('Paid', 'Paid'),
    ('Pending', 'Pending'),
]

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # hashes password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=10, null=True, blank=True)
    action = models.CharField(max_length=4, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # For admin site access

    groups = models.ManyToManyField(
        Group,
        related_name="custom_users_groups",  # custom related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_users_permissions",  # custom related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


    USERNAME_FIELD = 'email'  # Use email to login
    REQUIRED_FIELDS = ['firstname', 'lastname']

    objects = UserManager()

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.email})"


class Category(models.Model):
    CategoryID=models.IntegerField(primary_key=True)
    CategoryName=models.CharField(max_length=50)
    CategoryDescription=models.CharField(max_length=255)

    def __str__(self):
        return self.CategoryName

  
class Products(models.Model):
    ProductID=models.CharField(max_length=10,primary_key=True)
    ProductName=models.CharField(max_length=50)
    ProductDesc=models.CharField(max_length=255)
    Price=models.DecimalField(max_digits=10,decimal_places=2)
    size=models.CharField(max_length=20)
    stock=models.IntegerField()
    CategoryID=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    Added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Product {self.ProductID}-Name: {self.ProductName}"

class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

class Cart(models.Model):
    CartID=models.CharField(max_length=10,primary_key=True)
    UserID=models.ForeignKey(Users,on_delete=models.SET_NULL,null=True,blank=True)
    ProductID=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,blank=True)
    Quantity=models.IntegerField(default=1)
    Added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"cart{self.CartID}- User: {self.UserID} - Product: {self.ProductID}"

  
class Invoice(models.Model):
    DocheaderNo=models.AutoField(primary_key=True)
    UserID=models.ForeignKey(Users,on_delete=models.SET_NULL,null=True,blank=True)
    Discount=models.DecimalField(max_digits=10,decimal_places=2)
    Tax=models.DecimalField(max_digits=10,decimal_places=2)
    Beforetax=models.DecimalField(max_digits=10,decimal_places=2)
    Aftertax=models.DecimalField(max_digits=10,decimal_places=2)
    Paymentstatus=models.CharField(max_length=20,choices=PAYMENT_STATUS_CHOICES,default='Unpaid')
    BillingAddress=models.CharField(max_length=255)

    def __str__(self):
        return f"Invoice {self.DocheaderNo}-User: {self.UserID}"



class InvoiceDetails(models.Model):
    DocheaderNo=models.AutoField(primary_key=True)
    UserID=models.ForeignKey(Users,on_delete=models.SET_NULL,null=True,blank=True)
    InvNo=models.ForeignKey(Invoice,on_delete=models.SET_NULL,null=True,blank=True)
    ProductID=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,blank=True)
    Tax=models.DecimalField(max_digits=10,decimal_places=2)
    Quantity=models.IntegerField()
    Price=models.DecimalField(max_digits=10,decimal_places=2)
    GST=models.CharField(max_length=30)

    def __str__(self):
        return f"InvoiceDetails {self.DocheaderNo}"


class Payments(models.Model):
    DocNo=models.IntegerField(primary_key=True)
    InvoiceNO=models.ForeignKey(Invoice,on_delete=models.SET_NULL,null=True,blank=True)
    PaymentMethod=models.CharField(max_length=4)
    Amount=models.DecimalField(max_digits=10,decimal_places=2)
    PayementDate=models.DateTimeField(default=timezone.now)
    PaymentStatus=models.CharField(max_length=6)

    def __str__(self):
        return f"Payment {self.DocNo}"


class Coupouns(models.Model):
    ID=models.IntegerField(primary_key=True)
    Code=models.CharField(max_length=20,unique=True)
    method=models.CharField(max_length=2,default='01')
    DiscountPercent=models.CharField(max_length=2,default='01')
    ValidFrom=models.DateTimeField(default=timezone.now)
    validTill=models.DateField
    ISActive=models.BooleanField(default=1)

    def __str__(self):
        return self.Code

  

class Customer(models.Model):
    ID=models.CharField(max_length=10,primary_key=True)
    UserID=models.IntegerField()
    Addressline1=models.CharField(max_length=255)
    Addressline2=models.CharField(max_length=255,null=True)
    CustomerState=models.CharField(max_length=50)
    Postalcode=models.CharField(max_length=20)
    created=models.DateTimeField(default=timezone.now)
    GSt=models.CharField(max_length=50)

    def __str__(self):
        return f"Customer {self.ID}"



