# Chat Admin - Updated November 2025
# Django admin configuration for chat rooms and messages

from django.contrib import admin
from .models import Chat, Room

admin.site.register(Chat)
admin.site.register(Room)
