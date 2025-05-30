from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.templatetags.static import static
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def adminpanel(request):
    return render(request,'Admin/Admin_navbar.html')

def admin_user(request):
    return render(request,'Admin/Admin_user.html')
def admin_products(request):
    return render(request,'Admin/Admin_index.html')

def admin_offers(request):
    return render(request,'Admin/Admin_index.html')

def admin_ordes(request):
    return render(request,'Admin/Admin_index.html')

def admin_customers(request):
    return render(request,'Admin/Admin_index.html')
def admin_reports(request):
    return render(request,'Admin/Admin_index.html')
def add_user(request):
    return render(request,'Admin/Admin_index.html')