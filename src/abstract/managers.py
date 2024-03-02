from django.db import models


class BaseManager(models.Manager):
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

    def get_queryset(self):
        """
        Returns the base queryset.
        """
        return super().get_queryset()

    def all(self):
        """
        Returns all objects excluding those with status=False.
        """
        return super().all().exclude(status=False)

    def filter(self, *args, **kwargs):
        """
        Filters objects based on given conditions, excluding those with status=False.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            QuerySet: A filtered queryset.
        """
        return super().filter(*args, **kwargs).exclude(status=False)

    def count(self):
        """
        Returns the count of objects excluding those with status=False.
        """
        return self.filter().count()
