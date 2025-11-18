# Friend Utilities - Updated November 2025
# Helper functions for friend request management

from friend.models import FriendRequest

def get_friend_request_or_false(sender, receiver):
    try:
        return FriendRequest.objects.get(sender=sender, receiver=receiver, is_active=True)
    except FriendRequest.DoesNotExist:
        return False