from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="superuser").exists():
            User.objects.create_superuser("superuser", "super@user.com", "apptitud")