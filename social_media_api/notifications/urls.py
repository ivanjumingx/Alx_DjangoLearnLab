from django.urls import path
from .views import NotificationList, MarkAsRead

urlpatterns = [
    path('notifications/', NotificationList.as_view(), name='notification_list'),
    path('notifications/<int:notification_id>/read/', MarkAsRead.as_view(), name='mark_as_read'),
]
