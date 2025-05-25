from django.shortcuts import render,redirect,HttpResponse
from django.templatetags.static import static
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Users,Cart,Category,Coupouns,Customer,Payments,Products,Invoice,InvoiceDetails
import hashlib
# Create your views here.

def home(request):
    slides = [
        static("banner1.png"),
        static("banner2.png"),
        static("banner3.jpg"),
    ]
    return render(request, "index.html", {"slides": slides})

def profile(request):
    return render(request,'profile.html')

def orders(request):
    return render(request,'orders.html')

def coupons(request):
    return render(request,'offers/coupons.html')

def signup(request):
    if request.method=='POST':
        firstname=request.Post['fname']
        lastname=request.post['Lname']
        email=request.post['email']
        passw=request.post['password']
        phone=request.post['phone']
        role='Customer'
        action='0001'
        msg_code=''
        hashed_password = hashlib.sha256(passw.encode()).hexdigest() #import haslib

        if Users.objects.filter(email=email):
            msg_code='100'
            messages.error(request,"UserName Already exist")
            return render(request, 'User/login.html')
        myuser=Users(Firstname=firstname,
                     Lastname=lastname, 
                     email=email,
                     password=hashed_password,
                     phone=phone,
                     created=timezone.now()) #import timezone)
        myuser.save()
        msg_code='111'
        messages.success(request, "Account created successfully! Please login.")
        return redirect('User/login.html')

    return render(request,'User/signup.html')

def address_list(request):
    return render(request,'User/address_list.html')
def login(request):
    return render(request,'User/login.html')

def otp(request):
    return render(request,'otp.html')

def pass_word(request):
    return render(request,'password.html')

def password_change(request):
    return render(request,'change_pass.html')

def upd_sec(request):
    return render(request,'upd_security.html')

def accounts(request):
    return render(request,'User/Accounts.html')

def wishlist(request):
    return render(request,'wishlist.html')

def cart(request):
    return render(request,'cart.html')

def productsmain(request):
    return render(request,'products/product_main.html')