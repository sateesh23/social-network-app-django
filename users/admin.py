# Users Admin - Updated November 2025
# Django admin configuration for user profiles and relationships

from django.contrib import admin
from .models import Profile, Relationship

admin.site.register(Profile)
admin.site.register(Relationship)
