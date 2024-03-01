from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    USERNAME_FIELD = "username"

    mobile_no = CharField(unique=True, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username

    def get_full_name(self):
        return (
            self.username
            if not self.first_name and not self.last_name
            else f"{self.first_name} {self.last_name}"
        )

    def delete(self, *args, **kwargs):
        if self.is_staff:
            self.is_staff = False
            self.save()

    class Meta:
        managed = settings.MANAGE_DATABASE
        db_table = "user"
        verbose_name_plural = "Users"
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []
