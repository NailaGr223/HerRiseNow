from django.shortcuts import render, redirect
from django.contrib import messages
from .models import careermentorshipform, peermentorshipform, learnform, userappform, partnerappform, sponsorappform, adminappform, contactform, counselingform


def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contactform(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name') 
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contactform.objects.create(
                 full_name=full_name,
                 email=email,
                 subject=subject,
                 message=message
          )
        return redirect('contact')
    return render(request, 'contact.html')
def careermentorshipform(request):
   if request.method == 'POST':
      full_name = request.POST.get('full_name') 
      email = request.POST.get('email')
      phone_number = request.POST.get('phone_number')
      preferred_mentor = request.POST.get('preferredmentor')
      currentcareerstage = request.POST.get('currentcareerstage')
      goals = request.POST.get('goals')
      anything_else = request.POST.get('anythingelse')
      careermentorshipform.objects.create(
             full_name=full_name,
             email=email,
             phone_number=phone_number,
             preferred_mentor=preferred_mentor,
             currentcareerstage=currentcareerstage,
             goals=goals,
             anything_else=anything_else
        )
      return redirect('mentorship')
   return render(request, 'careermentorshipform.html')


def peermentorshipform(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name') 
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        preferred_mentor = request.POST.get('preferredmentor')
        age_range = request.POST.get('agerange')
        areaofgrowth = request.POST.get('areaofgrowth')
        peermentorshipform.objects.create(
                 full_name=full_name,
                 email=email,
                 phone_number=phone_number,
                 preferred_mentor=preferred_mentor,
                 age_range=age_range,
                 areaofgrowth=areaofgrowth
          )
        return redirect('mentorship')
    return render(request, 'peermentorshipform.html')
    
def chooseyourcareermentor(request):
    return render(request, 'chooseyourcareermentor.html')
def chooseyourpeermentor(request):
    return render(request, 'chooseyourpeermentor.html')
def community(request):
    return render(request, 'community.html')
def counseling(request):
    return render(request, 'counseling.html')
def counselingform(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name') 
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        preferred_counselor = request.POST.get('preferredcounselor')
        what_brings_you_here = request.POST.get('whatbringsyouhere')
        tell_us_more = request.POST.get('tellusmore')
        preferred_schedule = request.POST.get('preferredschedule')
        counselingform.objects.create(
                 full_name=full_name,
                 email=email,
                 phone_number=phone_number,
                 preferred_counselor=preferred_counselor,
                 what_brings_you_here=what_brings_you_here,
                 tell_us_more=tell_us_more,
                 preferred_schedule=preferred_schedule
          )
        return redirect('counseling')
    return render(request, 'counselingform.html')
def learn(request):
    return render(request, 'learn.html')
def learnform(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name') 
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        currenteducation_level = request.POST.get('currenteducationlevel')
        topics_of_interest = request.POST.get('topicsofinterest')
        other_topics = request.POST.get('othertopics')
        preffered_learning_style = request.POST.get('prefferedlearningstyle')
        availability = request.POST.get('availability')
        learnform.objects.create(
                 full_name=full_name,
                 email=email,
                 phone_number=phone_number,
                 currenteducation_level=currenteducation_level,
                 topics_of_interest=topics_of_interest,
                 other_topics=other_topics,
                 preffered_learning_style=preffered_learning_style,
                 availability=availability
          )
        return redirect('learn')
    return render(request, 'learnform.html')
def login(request):
    return render(request, 'login.html')
def mentorship(request):
    return render(request, 'mentorship.html')
def ourprograms(request):
    return render(request, 'ourprograms.html')
def register(request):
    return render(request, 'register.html')
def userappform(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name') 
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        userappform.objects.create(
                 full_name=full_name,
                 email=email,
                 username=username,
                 password=password,
                 confirm_password=confirm_password
          )
        return redirect('register')
    return render(request, 'userappform.html')
def partnerappform(request):
    if request.method == 'POST':
        your_name = request.POST.get('yourname') 
        email = request.POST.get('email')
        organization_name = request.POST.get('organizationname')
        mission_statement = request.POST.get('missionstatement')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        partnerappform.objects.create(
                 your_name=your_name,
                 email=email,
                 organization_name=organization_name,
                 mission_statement=mission_statement,
                 password=password,
                 confirm_password=confirm_password
          )
        return redirect('register')
    return render(request, 'partnerappform.html')
def sponsorappform(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name') 
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        choose_amount = request.POST.get('chooseamount')
        sponsorappform.objects.create(
                 full_name=full_name,
                 email=email,
                 phone_number=phone_number,
                 password=password,
                 confirm_password=confirm_password,
                 choose_amount=choose_amount
          )
        return redirect('register')
    return render(request, 'sponsorappform.html')
def adminappform(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name') 
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        reason_for_access = request.POST.get('reasonforaccess')
        adminappform.objects.create(
                 full_name=full_name,
                 email=email,
                 password=password,
                 confirm_password=confirm_password,
                 reason_for_access=reason_for_access
          )
        return redirect('register')
    return render(request, 'adminappform.html')
# def contactform(request):
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name') 
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         contactform.objects.create(
#                  full_name=full_name,
#                  email=email,
#                  subject=subject,
#                  message=message
#           )
#         return redirect('contact')
#     return render(request, 'contactform.html')
def contact(request):
    return render(request, 'contact.html')


