from django.core.management import BaseCommand

from users.models import User
import os
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    """Command used to create users with different level of permissions.
    For admin user you must use your real email, it needs to receive registration email"""

    def handle(self, *args, **options):
        admin = User.objects.create(
            email=os.getenv("PERSONAL_EMAIL"),
            first_name='Admin',
            last_name='Adminov',
            role='moderator',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        admin.set_password(os.getenv("SUPERUSER_PASSWORD"))
        admin.save()

        moderator = User.objects.create(
            email='moderator@sky.pro',
            first_name='Moderator',
            last_name='Moderatov',
            role='moderator',
            is_staff=True,
            is_superuser=False,
            is_active=True
        )

        moderator.set_password(os.getenv("MODERATOR_PASSWORD"))
        moderator.save()

        member = User.objects.create(
            email='member@sky.pro',
            first_name='Member',
            last_name='Memberov',
            role='member',
            is_staff=False,
            is_superuser=False,
            is_active=True
        )

        member.set_password(os.getenv("MEMBER_PASSWORD"))
        member.save()
