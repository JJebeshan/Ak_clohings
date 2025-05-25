import math
import random
from django.shortcuts import render,redirect,HttpResponse
from django.templatetags.static import static
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
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
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        passw = request.POST.get('password')
        phone = request.POST.get('phone')
        role='Customer'
        action='0001'
        msg_code=''
        hashed_password = hashlib.sha256(passw.encode()).hexdigest() #import haslib
        if Users.objects.filter(email=email).exists():
            msg_code='100'
            messages.error(request,"UserName Already exist")
            return render(request, 'User/login.html')
        myuser = Users(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=hashed_password,
            phone=phone,
            created=timezone.now(),
            role=role,
            action=action
        )
        myuser.save()
        usr_msg=(
            "Thanks for signing up! \n\n"
        "This is an auto-generated email. Please do not reply. \n\n"
        "Use this coupon code **WEL100** for your first shopping! 🎉 \n\n"
        "Thanks and regards,\n"
        "Akshana"
        )
        send_mail(subject='Welcome to My Akshana Clothings!',
        message=usr_msg,
        from_email='akshanaclothings@gmail.com',
        recipient_list=[email],
        fail_silently=False,) 
  

        msg_code='111'
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request,'User/signup.html')

def address_list(request):
    return render(request,'User/address_list.html')
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        if Users.objects.filter(email=email).exists():
            request.session['user_email'] = email
            return render(request,'password.html')
        else:
            messages.error(request,"User Not Found")
    return render(request,'User/login.html')

def otp(request):
    if request.method=='POST':
        one=request.Post.get('fst')
        two=request.Post.get('scd')
        three=request.Post.get('thrd')
        four=request.Post.get('frt')
        five=request.Post.get('fv')
        six=request.Post.get('sx')
        otp=one+two+three+four+five+six
        vrf=request.session['otp']
        if vrf==otp:
            return render(request,'index.html')
        else:
            messages.error(request,"Enter a Valid OTP ")

    return render(request,'otp.html')

def otp_veri(request):
    rand=random.randint(100000, 999999)
    request.session['otp']=str(rand)
    email = request.session.get('user_email')
    usr_msg=("Greetings From Akshana \n\n"
             f"OTP for login {rand}")
    send_mail(subject='Welcome to My Akshana Clothings!',
        message=usr_msg,
        from_email='akshanaclothings@gmail.com',
        recipient_list=[email],
        fail_silently=False,) 
  
    return render(request,'otp.html')


def pass_word(request):
    email=request.session['user_email']
    if not email:
        return redirect('login')
    if request.method=='POST':
        password=request.POST.get('password')
        hashed_input=hashlib.sha256(password.encode()).hexdigest()
        try:
            user=Users.objects.get(email=email)
            if user.password==hashed_input:
                messages.success(request,"Success")
                return redirect('home')
            else:
                messages.error(request,"inccorrect password or Invalid Username")
        except Users.DoesNotExist:
            messages.error(request,"Invlaid user")
            return redirect('login')
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

def logout(request):
    request.session.flush()
    messages.success(request,"Logout sucess")
    return render(request,'index.html')