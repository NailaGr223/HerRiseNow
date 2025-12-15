# community/admin.py
from django.contrib import admin
from .models import *
admin.site.register(CareerMentorship)
admin.site.register(PeerMentorship) 
admin.site.register(Learn)
admin.site.register(Contact)
admin.site.register(Counseling)
admin.site.register(Post)

