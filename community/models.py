from django.db import models

# Create your models here.
class CareerMentorship(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    preferred_mentor = models.CharField(max_length=200)
    currentcareerstage = models.CharField(max_length=200)
    goals = models.TextField()
    anything_else = models.TextField(max_length=500, blank=True,null=True)

    def __str__(self):
        return self.full_name
    
class PeerMentorship(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    preferred_mentor = models.CharField(max_length=200)
    age_range = models.CharField(max_length=100)
    areaofgrowth = models.TextField()

    def __str__(self):
        return self.full_name
    
class Learn(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    currenteducation_level = models.CharField(max_length=200)
    topics_of_interest = models.TextField()
    other_topics = models.TextField(max_length=500, blank=True, null=True)
    preffered_learning_style = models.CharField(max_length=200)
    availability = models.CharField(max_length=200)
    

    def __str__(self):
        return self.full_name
    


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    
class Counseling(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    preferred_counselor = models.CharField(max_length=200)
    what_brings_you_here = models.TextField()
    tell_us_more = models.TextField(max_length=500, blank=True, null=True)
    preferred_schedule = models.CharField(max_length=200)
    

    def __str__(self):
        return self.full_name
    
class Post(models.Model):
    content = models.TextField()
    poster = models.CharField(max_length=100, blank=True, null=True, default="Anonymous")

    def __str__(self):
        return self.poster

class Donation(models.Model):
    
    phone_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(self):
        return f"{self.full_name} - {self.amount} ({self.frequency})"