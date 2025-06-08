from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.templatetags.static import static
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from AKC.models import Users,Invoice,Products,ProductImage,Category
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
    categories = Category.objects.all()
    if not Products.objects.exists():
        id='001'
    else:
        last=Products.objects.last()
        id=int(last.ProductID)+int(1)
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('description')
        price=request.POST.get('price')
        Stock=request.POST.get('stock')
        xs = request.POST.get('XS')
        s = request.POST.get('S') # ['S', 'M', 'L']
        m = request.POST.get('M')
        l = request.POST.get('L')
        xl = request.POST.get('XL')
        xxl = request.POST.get('XXL')
        sizes = xs+s+m+l+xl+xxl
        category=request.POST.get('category_id')
        images = request.FILES.getlist('images')
        try:
            category = Category.objects.get(pk=category)
        except Category.DoesNotExist:
            # Handle case where category does not exist
            return HttpResponse("Invalid Category", status=400)

        
        product=Products.objects.create(
            ProductID=id,
            ProductName=name,
            ProductDesc=desc,
            Price=price,
            stock=Stock,
            size=sizes,
            CategoryID=category

        )
        for img in images:
            ProductImage.objects.create(product=product, image=img)
        return redirect('admin_products') 
    messages.success(request, "User created successfully")    
    return render(request,'Admin/admin_products.html',{'categories':categories})

def admin_offers(request):
    return render(request,'Admin/Admin_index.html')

def admin_orders(request):
    return render(request,'Admin/Admin_index.html')

def admin_catgeory(request):
    if not Category.objects.exists():
        last_id='001'
    else:
        last=Category.objects.last()
        last_id=int(last.CategoryID)+int(1)
    if request.method=='POST':
        id=request.POST.get('category_id')
        name=request.POST.get('name')
        desc=request.POST.get('description')

        categ=Category(
            CategoryID=id,
            CategoryName=name,
            CategoryDescription=desc

        )
        categ.save()
    return render(request,'Admin/category.html',{'categoryid':last_id})
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
