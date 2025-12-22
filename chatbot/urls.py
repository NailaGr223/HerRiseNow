from django.urls import path
from .views import ai_chatbot 

urlpatterns = [
    path('ai-chatbot/', ai_chatbot, name='ai_chatbot'), 
]