from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rolepermissions.roles import assign_role
from .roles import Admin, Partner, Sponser, User

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        extra_fields.setdefault('role', 'admin') 

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('partner', 'Partner'),
        ('sponser', 'Sponser'),
        ('user', 'User'),
    ]

    username = models.CharField(max_length=150, blank=True, null=True, unique=False)

    email = models.EmailField(max_length=191, unique=True) 
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True) 

    company_name = models.CharField(max_length=100, blank=True, null=True)
    institution_name = models.CharField(max_length=100, blank=True, null=True)
    services_offered = models.TextField(blank=True, null=True)
    
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='user')  

    objects = CustomUserManager()  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.assign_role_permissions()

    def assign_role_permissions(self):
        role_mapping = {
            'admin': Admin,
            'partner': Partner,
            'sponser': Sponser,
            'user': User,
        }

        role_class = role_mapping.get(self.role.lower())  
        if role_class:
            assign_role(self, role_class)
        else:
            assign_role(self, User)

    def __str__(self):
        return self.email or self.username or "No Email"

