from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.templatetags.static import static
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from AKC.models import Users,Invoice
import hashlib

# Create your views here.
def adminpanel(request):
    return render(request,'Admin/Admin_navbar.html')

def admin_user(request):
    customer=Users.objects.filter(role='Customer').count
    staff=Users.objects.exclude(role='Customer').count
    orders=Invoice.objects.count()
    return render(request,'Admin/Admin_user.html',{'customers':customer,'staff':staff,'orders':orders})
def admin_products(request):
    return render(request,'Admin/admin_products.html')

def admin_offers(request):
    return render(request,'Admin/Admin_index.html')

def admin_orders(request):
    return render(request,'Admin/Admin_index.html')

def admin_customers(request):
    return render(request,'Admin/Admin_index.html')
def admin_reports(request):
    return render(request,'Admin/Admin_index.html')
def add_user(request):
     
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        passw = request.POST.get('password')
        role = request.POST.get('role')
        admin = request.POST.get('admin', '')
        sales = request.POST.get('sales', '')
        accounts = request.POST.get('accounts', '')
        support = request.POST.get('support', '')

        action = admin + sales + accounts + support
        hash_pwd = hashlib.sha256(passw.encode()).hexdigest()

        if Users.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'User/login.html')

        parts = username.strip().split(' ', 1)
        if len(parts) == 2:
            firstname, lastname = parts
        else:
            firstname = parts[0]
            lastname = ''
        myuser = Users(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=hash_pwd,
            phone=phone,
            created=timezone.now(),
            role=role,
            action=action
        )
        myuser.save()  # Save the user to the database

        messages.success(request, "User created successfully")
        return redirect('add_user')  # or another success page/view

    return render(request, 'Admin/add_user.html')
