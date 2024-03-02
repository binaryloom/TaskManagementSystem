from django.conf import settings
from django.db import models

from abstract.managers import BaseManager
from user.models import User


class BaseModel(models.Model):
    """
    This is the base class model for all models of the database tables.

    Attributes:
        operating_user (object): The user operating on the model instance.
        objects (BaseManager): The custom manager for BaseModel instances.
        status (bool): Status of the record (active or not), default is True.
        created_at (DateTime): Datetime of creation, auto-generated.
        updated_at (DateTime): Last modification datetime, auto-updated.
        created_by (ForeignKey): User who created the record.
        updated_by (ForeignKey): User who last updated the record.

    Usage:
        class <CLASS_NAME>(BaseModel):
            # model definition
    """

    operating_user = None

    objects = BaseManager()

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    created_by = models.ForeignKey(
        "user.User",
        related_name="%(class)s_created_by",
        on_delete=models.DO_NOTHING,
        blank=True,
    )
    updated_by = models.ForeignKey(
        "user.User",
        related_name="%(class)s_updated_by",
        on_delete=models.DO_NOTHING,
        blank=True,
    )

    def save(self, *args, **kwargs):
        """
        Save method overridden to set created_by and updated_by fields.
        """
        operating_user = (
            self.operating_user if hasattr(self, "operating_user") else None
        )
        self.updated_by = operating_user
        if not self.pk:
            self.created_by = operating_user
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Override delete method to set status to False instead of actual deletion.
        """
        self.status = False
        self.save(*args, **kwargs)

    class Meta:
        """
        Meta class to specify metadata options for the BaseModel.
        """

        abstract = True
        ordering = ["-updated_at"]
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []
