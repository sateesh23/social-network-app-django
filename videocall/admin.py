# Videocall Admin - Updated November 2025
# Django admin configuration for video call room members

from django.contrib import admin

# Register your models here.
from .models import RoomMember


admin.site.register(RoomMember)