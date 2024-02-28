from django.db import models

# from user.models import User
# from versity_info.enums import CellSize
# from versity_info.abstract_managers import BaseManager
# from phonenumber_field import modelfields
from django.conf import settings


class BaseClass(models.Model):
    """This is the base class model for all of the database tables.

    Contains:
        created_on = Datetime of creation.
        updated_on = Last modification datetime.
        created_by = Created by which user.
        updated_by = User who lastly modified.
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
        User,
        related_name="created_by_%(class)s",
        on_delete=models.DO_NOTHING,
        blank=True,
    )
    updated_by = models.ForeignKey(
        User,
        related_name="updated_by_%(class)s",
        on_delete=models.DO_NOTHING,
        blank=True,
    )
