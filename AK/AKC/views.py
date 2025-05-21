from django.shortcuts import render,redirect,HttpResponse
from django.templatetags.static import static
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
    return render(request,'signup.html')

def address_list(request):
    return render(request,'User/address_list.html')
def login(request):
    return render(request,'login.html')

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