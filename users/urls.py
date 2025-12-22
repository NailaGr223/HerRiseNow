from django.contrib import admin
from django.urls import path, include
from users import views
from users.views import register_view, dashboard_view, profile_view

urlpatterns = [
    path('login/', views.login_view, name='login'),
    # path('register/', views.register, name='register'),
    path('donation/', views.donation, name='donation'),
    path('logout/', views.logout_view, name='logout'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile'),


]
