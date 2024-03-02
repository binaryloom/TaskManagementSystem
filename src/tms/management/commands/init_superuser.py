from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            if settings.ADMINS != None:
                superuser = settings.ADMINS["default"]
                User.objects.create_superuser(
                    superuser["USER"], superuser["EMAIL"], superuser["PASSWORD"]
                )
        else:
            print("Admin accounts can only be initialized if no Accounts exist")
