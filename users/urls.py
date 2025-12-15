from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('donation/', views.donation, name='donation'),
    path('logout/', views.logout_view, name='logout'),
    


]
