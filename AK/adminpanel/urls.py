from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.adminpanel,name='adminpanel'),
    path('admin-users',views.admin_user,name='admin-users'),
    path('admin-products',views.admin_user,name='admin-products'),
    path('admin-offers',views.admin_user,name='admin-offers'),
    path('admin-orders',views.admin_user,name='admin-orders'),
    path('admin-customers',views.admin_user,name='admin-customers'),
    path('admin-report',views.admin_user,name='admin-report'),
    path('add-user',views.add_user,name='add-user'),
]