from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification

class NotificationList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.all().order_by('-timestamp')
        unread_count = notifications.filter(read=False).count()
        notification_data = [
            {
                "id": notification.id,
                "actor": notification.actor.username,
                "verb": notification.verb,
                "target": str(notification.target),
                "timestamp": notification.timestamp,
                "read": notification.read,
            }
            for notification in notifications
        ]
        return Response({
            "notifications": notification_data,
            "unread_count": unread_count
        }, status=status.HTTP_200_OK)

class MarkAsRead(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, notification_id):
        try:
            notification = Notification.objects.get(pk=notification_id, recipient=request.user)
            notification.read = True
            notification.save()
            return Response({"message": "Notification marked as read."}, status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response({"error": "Notification not found."}, status=status.HTTP_404_NOT_FOUND)
