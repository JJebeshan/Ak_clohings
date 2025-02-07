from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
   path('',views.home, name='home'),
   path('profile',views.profile,name='profile'),
   path('orders',views.orders, name='orders'),
   path('coupons',views.coupons,name='coupons'),
   path('signup',views.signup,name='signup'),
   path('address_list',views.address_list,name='address_list'),
   path('login',views.login,name='login'),
   path('otp',views.otp,name='otp'),
   path('password',views.pass_word,name='password'),
   path('changepass',views.password_change,name='changepas'),
   path('upd_sec',views.upd_sec,name='updatesecurity'),
   path('Accounts',views.accounts,name='accounts'),
   path('wishlist',views.wishlist,name='wishlist'),
   path('cart',views.cart,name='cart'),
]