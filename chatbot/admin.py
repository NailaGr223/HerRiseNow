from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'session_id', 'user', 'message', 'reply')
    list_filter = ('timestamp', 'user')
    search_fields = ('message', 'reply')
    readonly_fields = ('timestamp',)