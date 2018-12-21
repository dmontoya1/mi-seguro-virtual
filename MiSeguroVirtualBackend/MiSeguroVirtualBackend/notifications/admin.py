

from django.contrib import admin, messages
from django.contrib.auth import get_user_model

from users.models import User
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    model = Notification
    icon = '<i class="material-icons">notifications</i>'
    list_display = ('id', 'title', 'description', 'date', 'user')

    class Media:
        js = (
            'js/admin/notification_admin.js',
        )

    search_fields = (
        'date', 'title', 'description', 'user__first_name', 'user__last_name', 'user__document_id'
    )

    fieldsets = (
        (None, {
            'fields': (
                'title', 'description', 'user'
            ),
        }),
    )