from django.db import models

# Create your models here.
class careermentorshipform(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    preferred_mentor = models.CharField(max_length=200)
    currentcareerstage = models.CharField(max_length=200)
    goals = models.TextField()
    anything_else = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.full_name
    
class peermentorshipform(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    preferred_mentor = models.CharField(max_length=200)
    age_range = models.CharField(max_length=100)
    areaofgrowth = models.TextField()

    def __str__(self):
        return self.full_name
    
class learnform(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    currenteducation_level = models.CharField(max_length=200)
    topics_of_interest = models.TextField()
    other_topics = models.TextField(max_length=500, blank=True)
    preffered_learning_style = models.CharField(max_length=200)
    availability = models.CharField(max_length=200)
    

    def __str__(self):
        return self.full_name
    
class userappform(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)

    def __str__(self):
        return self.full_name
    
class partnerappform(models.Model):
    your_name = models.CharField(max_length=200)
    email = models.EmailField()
    organization_name = models.CharField(max_length=200)
    mission_statement = models.TextField()
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)

    def __str__(self):
        return self.organization_name
    
class sponsorappform(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    choose_amount = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
class adminappform(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    reason_for_access = models.TextField()

    def __str__(self):
        return self.full_name
    

class contactform(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    
class counselingform(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    preferred_counselor = models.CharField(max_length=200)
    what_brings_you_here = models.TextField()
    tell_us_more = models.TextField(max_length=500, blank=True)
    preferred_schedule = models.CharField(max_length=200)
    

    def __str__(self):
        return self.full_name