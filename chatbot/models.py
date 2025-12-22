# chatbot/models.py
from django.db import models
from django.contrib.auth.models import User  # Optional: if you want to link to logged-in users

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Optional: link to user
    session_id = models.CharField(max_length=50, blank=True)  # Unique per session (anonymous users)
    message = models.TextField()  # User's message
    reply = models.TextField()    # Bot's reply
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat at {self.timestamp}"

    class Meta:
        ordering = ['timestamp']