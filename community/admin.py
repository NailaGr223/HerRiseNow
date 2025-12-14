# community/admin.py
from django.contrib import admin
from .models import careermentorshipform, peermentorshipform, learnform, userappform, partnerappform, sponsorappform, adminappform, contactform, counselingform
admin.site.register(careermentorshipform)
admin.site.register(peermentorshipform) 
admin.site.register(learnform)
admin.site.register(userappform)
admin.site.register(partnerappform)
admin.site.register(sponsorappform)
admin.site.register(adminappform)
admin.site.register(contactform)
admin.site.register(counselingform)
