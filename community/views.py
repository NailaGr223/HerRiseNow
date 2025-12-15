from django.shortcuts import render, redirect
from django.contrib import messages
from community.models import * 

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
        Contact.objects.create(
                 full_name=full_name,
                 email=email,
                 subject=subject,
                 message=message
          )
        return redirect('index')
    return render(request, 'contact.html')
def careermentorshipform(request):
   if request.method == 'POST':
      full_name = request.POST.get('full_name') 
      email = request.POST.get('email')
      phone_number = request.POST.get('phone_number')
      preferred_mentor = request.POST.get('preferred_mentor') 
      currentcareerstage = request.POST.get('currentcareerstage')
      goals = request.POST.get('goals')
      anything_else = request.POST.get('anythingelse')
      CareerMentorship.objects.create(
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
        preferred_mentor = request.POST.get('preferred_mentor')
        age_range = request.POST.get('age_range')
        areaofgrowth = request.POST.get('areaofgrowth')
        PeerMentorship.objects.create(
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

    posts= Post.objects.all()
    context={'posts':posts}
    if request.method == 'POST':
        content = request.POST.get('content')
        poster = request.POST.get('poster') or "Anonymous"
        Post.objects.create(
            content=content,
            poster=poster
        )
        return redirect('community')
    return render(request, 'community.html', context)
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('community')
def updatepost(request, post_id):

    post= Post.objects.get(id=post_id)
    context={'post':post}
    if request.method == 'POST':
        post.content = request.POST.get('content')
        post.save()
       
        
        
        return redirect('community')
    return render(request, 'postupdates.html', context)
def counseling(request):
    return render(request, 'counseling.html')
def counselingform(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name') 
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        preferred_counselor = request.POST.get('preferred_counselor')
        what_brings_you_here = request.POST.get('what_brings_you_here')
        tell_us_more = request.POST.get('tell_us_more')
        preferred_schedule = request.POST.get('preferred_schedule')
        Counseling.objects.create(
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
        currenteducation_level = request.POST.get('currenteducation_level')
        topics_of_interest = request.POST.get('topics_of_interest')
        other_topics = request.POST.get('other_topics')
        preffered_learning_style = request.POST.get('preffered_learning_style')
        availability = request.POST.get('availability')
        Learn.objects.create(
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

def mentorship(request):
    return render(request, 'mentorship.html')
def ourprograms(request):
    return render(request, 'ourprograms.html')


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
# def contact(request):
#     return render(request, 'contact.html')


