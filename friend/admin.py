# Friend Admin - Updated November 2025
# Django admin configuration for friend requests and friend lists

from django.contrib import admin
from friend.models import FriendList, FriendRequest

admin.site.register(FriendList)
admin.site.register(FriendRequest)
