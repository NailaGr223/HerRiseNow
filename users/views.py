from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from users.models import CustomUser
# from rolepermissions.roles import assign_role
from django_daraja.mpesa.core import MpesaClient
from users.roles import *
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import UserProgress, ActivityLog, Course
from .forms import ProfileEditForm
from .models import UserProfile


# def register(request):
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         first_name, last_name = (full_name.split(' ', 1) + [""])[:2]
#         institution = request.POST.get('institution')
#         service = request.POST.get('service')
#         company_name = request.POST.get('company_name')
        
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get
#         ('confirm_password')
#         role= request.POST.get('user_role')
#         print(full_name, institution, service, company_name, email, role, password, confirm_password)
#         print(first_name, last_name)

        

        # if password != confirm_password:
        #     messages.error(request, "Passwords do not match!")
        #     return render(request, 'register.html')  
        # print("Password match confirmed.")
        

        # if CustomUser.objects.filter(email=email).exists():
        #     messages.error(request, "This email is already registered.")
        #     return render(request, 'register.html')   
        # print("Email is unique, proceeding with registration.")
        
        

#         try:
#             user = CustomUser.objects.create_user(
#                 username=email,
#                 email=email,
                
#                 first_name=first_name,
#                 last_name=last_name,
#                 company_name=company_name,
#                 institution_name=institution,
#                 services_offered=service,
#                 role = role,
#             )
#             user.set_password(password)
#             user.save()
#             ROLE_MAP = {
#              "user": User,
#              "sponser": Sponser,
#              "partner": Partner,
#             }

#             assign_role(user, ROLE_MAP[user.role])

#             print("User created successfully:", user.email)

#             messages.success(request, f"Welcome, {first_name}! Your account has been created.")
#             return redirect('login')

#         except Exception as e:
#             print("Error creating user:", e)
#             messages.error(request, "Account creation failed. Please try again.")
#             return render(request, 'register.html')
#     return render(request, 'register.html')
# def donation(request):
#     return render(request, 'donation.html')
# def login_view(request):   
#     if request.method == 'POST':
#         email = request.POST.get('username')
#         password = request.POST.get('password')
#         print(email, password)
#         try:
#             user_obj = CustomUser.objects.get(email=email)
#             user = authenticate(
#                 request,
#                 username=user_obj.username,
#                 password=password
#             )
#             print("Authentication attempt for user:", email)
#             print("Password valid:", user_obj.check_password(password))

#         except User.DoesNotExist:
#             user = None
#         print("User object retrieved:", user)
#         if user is not None:
#             login(request, user) 
#             print("Login successful for user:", user.email)
#             if user.role == 'user':  # spelling fixed
#                 return redirect('donation')

#             return redirect('index')

#         messages.error(request, "Invalid email or password.")
#     return render(request, 'login.html')

# def logout_view(request):
#     logout(request)  
#     messages.success(request, "You have been logged out successfully.")
#     return redirect('login')
def donation(request):
    message = None
    error = None

    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        amount_str = request.POST.get('amount')

        # Basic validation
        if not phone_number or not amount_str:
            error = "Please fill in both phone number and amount."
        else:
            try:
                amount = int(amount_str)
                if amount < 1:
                    raise ValueError("Amount must be at least 1 KES")

                # Build callback URL properly
                callback_url = request.build_absolute_uri(reverse('mpesa_callback'))  # Better: use reverse()
                # OR if you don't have a named URL: request.build_absolute_uri('/mpesa_callback/')

                account_reference = "Donation"
                description = "Donation to Community"

                client = MpesaClient()
                response = client.stk_push(
                    phone_number=phone_number,
                    amount=amount,
                    account_reference=account_reference,
                    transaction_desc=description,
                    callback_url=callback_url
                )

                # response is usually a dict-like object
                if response.response_description == "Success":
                    message = "Payment request sent! Check your phone to complete via M-Pesa."
                else:
                    error = f"Request failed: {response.response_description}"

            except ValueError as e:
                error = "Invalid amount – must be a whole number (e.g., 100)"
            except Exception as e:
                error = f"M-Pesa error: {str(e)}"

    # This runs on GET or after POST (success/error)
    return render(request, 'donation.html', {
        'message': message,
        'error': error
    })

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! Please log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            ActivityLog.objects.create(user=user, action="Logged in")
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

@login_required
def dashboard_view(request):
    # Learning progress
    progress = UserProgress.objects.filter(user=request.user)
    completed_count = progress.filter(completed=True).count()
    total_courses = Course.objects.count()
    progress_percentage = (completed_count / total_courses * 100) if total_courses > 0 else 0

    # Recent activity
    activities = ActivityLog.objects.filter(user=request.user).order_by('-timestamp')[:10]

    context = {
        'progress': progress,
        'progress_percentage': progress_percentage,
        'activities': activities,
    }
    return render(request, 'users/dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def profile_view(request):
  profile, created = UserProfile.objects.get_or_create(user=request.user)

  if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated, Sister! 💜')
            return redirect('profile')
  else:
        form = ProfileEditForm(instance=profile, user=request.user)

  return render(request, 'users/profile.html', {'form': form})