from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.adminpanel,name='adminpanel'),
    path('admin-users',views.admin_user,name='admin-users'),
    path('admin_products',views.admin_products,name='admin_products'),
    path('admin-offers',views.admin_user,name='admin-offers'),
    path('admin-orders',views.admin_orders,name='admin-orders'),
    path('admin_category',views.admin_catgeory,name='admin_category'),
    path('admin-report',views.admin_user,name='admin-report'),
    path('add_user',views.add_user,name='add_user'),
]