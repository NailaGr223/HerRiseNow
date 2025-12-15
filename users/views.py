from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import CustomUser
from rolepermissions.roles import assign_role
from users.roles import *



def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        first_name, last_name = (full_name.split(' ', 1) + [""])[:2]
        institution = request.POST.get('institution')
        service = request.POST.get('service')
        company_name = request.POST.get('company_name')
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get
        ('confirm_password')
        role= request.POST.get('user_role')
        print(full_name, institution, service, company_name, email, role, password, confirm_password)
        print(first_name, last_name)

        

        # if password != confirm_password:
        #     messages.error(request, "Passwords do not match!")
        #     return render(request, 'register.html')  
        # print("Password match confirmed.")
        

        # if CustomUser.objects.filter(email=email).exists():
        #     messages.error(request, "This email is already registered.")
        #     return render(request, 'register.html')   
        # print("Email is unique, proceeding with registration.")
        
        

        try:
            user = CustomUser.objects.create_user(
                username=email,
                email=email,
                
                first_name=first_name,
                last_name=last_name,
                company_name=company_name,
                institution_name=institution,
                services_offered=service,
                role = role,
            )
            user.set_password(password)
            user.save()
            ROLE_MAP = {
             "user": User,
             "sponser": Sponser,
             "partner": Partner,
            }

            assign_role(user, ROLE_MAP[user.role])

            print("User created successfully:", user.email)

            messages.success(request, f"Welcome, {first_name}! Your account has been created.")
            return redirect('login')

        except Exception as e:
            print("Error creating user:", e)
            messages.error(request, "Account creation failed. Please try again.")
            return render(request, 'register.html')
    return render(request, 'register.html')
def donation(request):
    return render(request, 'donation.html')
def login_view(request):   
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        print(email, password)
        try:
            user_obj = CustomUser.objects.get(email=email)
            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )
            print("Authentication attempt for user:", email)
            print("Password valid:", user_obj.check_password(password))

        except User.DoesNotExist:
            user = None
        print("User object retrieved:", user)
        if user is not None:
            login(request, user) 
            print("Login successful for user:", user.email)
            if user.role == 'user':  # spelling fixed
                return redirect('donation')

            return redirect('index')

        messages.error(request, "Invalid email or password.")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)  
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

