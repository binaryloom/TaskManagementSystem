from django.db import models
from abstract.managers import BaseManager
from django.conf import settings


# from user.models import User
# from versity_info.enums import CellSize
# from versity_info.abstract_managers import BaseManager
# from phonenumber_field import modelfields


class BaseClass(models.Model):
    """This is the base class model for all of the database tables.

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

    class Meta:
        abstract = True
        ordering = ["-updated_at"]
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []
