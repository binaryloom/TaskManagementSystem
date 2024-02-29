from django.conf import settings
from django.db import models

from abstract.managers import BaseManager
from user.models import User


class BaseModel(models.Model):
    """This is the base class model for all  models of the database tables.

    Contains:
        created_on = Datetime of creation.
        updated_on = Last modification datetime.
        status = Status of a record active or not.

    Usage:
        class <CLASS_NAME> (BaseClass):
            # model definition
    """

    operating_user = None

    objects = BaseManager()

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    created_by = models.ForeignKey(
        "user.User",
        related_name="created_by",
        on_delete=models.DO_NOTHING,
        blank=True,
    )
    updated_by = models.ForeignKey(
        User,
        related_name="updated_by",
        on_delete=models.DO_NOTHING,
        blank=True,
    )

    def delete(self, *args, **kwargs):
        self.status = False
        self.save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ["-updated_at"]
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []
