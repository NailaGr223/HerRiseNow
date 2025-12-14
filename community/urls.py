from django.contrib import admin
from django.urls import path, include
from community import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contactform/', views.contactform, name='contactform'),
    path('careermentorshipform/', views.careermentorshipform, name='careermentorshipform'),
    path('peermentorshipform/', views.peermentorshipform, name='peermentorshipform'),
    path('chooseyourcareermentor/', views.chooseyourcareermentor, name='chooseyourcareermentor'),
    path('chooseyourpeermentor/', views.chooseyourpeermentor, name='chooseyourpeermentor'),
    path('community/', views.community, name='community'),
    path('counseling/', views.counseling, name='counseling'),
    path('counselingform/', views.counselingform, name='counselingform'),
    path('learn/', views.learn, name='learn'),
    path('learnform/', views.learnform, name='learnform'),
    path('login/', views.login, name='login'),
    path('mentorship/', views.mentorship, name='mentorship'),
    path('ourprograms/', views.ourprograms, name='ourprograms'),
    path('register/', views.register, name='register'),
    path('sponsorappform/', views.sponsorappform, name='sponsorappform'),
    path('partnerappform/', views.partnerappform, name='partnerappform'),
    path('userappform/', views.userappform, name='userappform'),
    path('adminappform/', views.adminappform, name='adminappform'),

    


]
