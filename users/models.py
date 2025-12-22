from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from rolepermissions.roles import assign_role
# from .roles import Admin, Partner, Sponser, User
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         extra_fields.setdefault('role', 'admin') 

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)
    
# class CustomUser(AbstractUser):
#     ROLE_CHOICES = [
#         ('admin', 'Admin'),
#         ('partner', 'Partner'),
#         ('sponser', 'Sponser'),
#         ('user', 'User'),
#     ]

#     username = models.CharField(max_length=150, blank=True, null=True, unique=False)

#     email = models.EmailField(max_length=191, unique=True) 
#     first_name = models.CharField(max_length=30, blank=True, null=True)
#     last_name = models.CharField(max_length=30, blank=True, null=True) 

#     company_name = models.CharField(max_length=100, blank=True, null=True)
#     institution_name = models.CharField(max_length=100, blank=True, null=True)
#     services_offered = models.TextField(blank=True, null=True)
    
#     role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='user')  

#     objects = CustomUserManager()  

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []  

#     def save(self, *args, **kwargs):
#         is_new = self.pk is None
#         super().save(*args, **kwargs)
#         if is_new:
#             self.assign_role_permissions()

#     def assign_role_permissions(self):
#         role_mapping = {
#             'admin': Admin,
#             'partner': Partner,
#             'sponser': Sponser,
#             'user': User,
#         }

#         role_class = role_mapping.get(self.role.lower())  
#         if role_class:
#             assign_role(self, role_class)
#         else:
#             assign_role(self, User)

#     def __str__(self):
#         return self.email or self.username or "No Email"
class Donation(models.Model):
    
    phone_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"{self.full_name} - {self.amount} ({self.frequency})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    progress_percentage = models.IntegerField(default=0)  # 0-100%
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)  # e.g., "Logged in", "Completed course"
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.action}"