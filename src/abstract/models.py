from django.db import models
from abstract.managers import BaseManager
from django.conf import settings


class BaseModelClass(models.Model):
    """This is the base class model for all of the database tables.

    Contains:
        created_on = Datetime of creation.
        updated_on = Last modification datetime.

    Usage:
        class <CLASS_NAME> (BaseModelClass):
            # model definition
    """

    objects = BaseManager()

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True
        ordering = ["-updated_at"]
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []


class BaseClass(BaseModelClass):
    """This is the base class model for all state full models of the database tables.

    Contains:
        created_on = Datetime of creation.
        updated_on = Last modification datetime.
        status = Status of a record active or not.

    Usage:
        class <CLASS_NAME> (BaseClass):
            # model definition
    """

    status = models.BooleanField(default=True)

    class Meta(BaseModelClass.Meta):
        pass
