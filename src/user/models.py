from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from versity_info.enums import CellSize, UserType

from .managers import UserManager

# Create your models here.


class User(AbstractUser):
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password"]
    objects = UserManager()
    mobile_no = models.CharField(
        unique=True, max_length=CellSize.MEDIUM, null=True, blank=True
    )
    user_type = models.CharField(
        choices=UserType, max_length=CellSize.XM, default=UserType.STUDENT  # type: ignore
    )

    def __str__(self):
        return self.username

    def get_full_name(self):
        return (
            self.username
            if not self.first_name and self.last_name
            else f"{self.first_name} {self.last_name}"
        )

    class Meta:
        managed = settings.MANAGE_DATABASE
        db_table = "task_board"
        verbose_name_plural = "Boards"
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []
