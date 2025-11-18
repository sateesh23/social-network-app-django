# Notification URLs - Updated November 2025
# URL routes for notification display and management

from django.urls import path
from notification.views import ShowNotifications

urlpatterns = [
    path('', ShowNotifications, name='show-notifications'),
]