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
    path('mentorship/', views.mentorship, name='mentorship'),
    path('ourprograms/', views.ourprograms, name='ourprograms'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('updatepost/<int:post_id>/', views.updatepost, name='updatepost'), 
    path('donation/', views.donation, name='donation'),
   

    


]
