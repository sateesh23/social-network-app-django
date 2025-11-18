# Blog Admin - Updated November 2025
# Django admin configuration for post and comment management

from django.contrib import admin
from .models import Comment, Post

admin.site.register(Post)
admin.site.register(Comment)
