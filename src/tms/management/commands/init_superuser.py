from django.conf import settings
from django.core.management.base import BaseCommand

from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            # Admin Setup
            username = "admin"
            email = "extinctCoder@outlook.com"
            password = "password"
            User.objects.create_superuser(username, email, password)
            self.stdout.write(
                self.style.SUCCESS("Super user account created successfully")
            )
            self.stdout.write(self.style.SUCCESS(f"username \t: {username}"))
            self.stdout.write(self.style.SUCCESS(f"password \t: {password}"))

        else:
            self.stdout.write(
                self.style.ERROR(
                    "Admin accounts can only be initialized if no Accounts exist"
                )
            )
