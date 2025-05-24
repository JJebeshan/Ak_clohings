from django.contrib import admin
from .models import Users,Cart,Category,Coupouns,Customer,Payments,Products
# Register your models here.
admin.site.register(Users)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Coupouns)
admin.site.register(Customer)
admin.site.register(Payments)
admin.site.register(Products)