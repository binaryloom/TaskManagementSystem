from django.db import models


class BaseManager(models.Manager):
    """
    A custom manager class for models with a 'status' field, providing methods for
    querying and filtering objects based on their status.

    Methods:
        get_queryset(): Returns the base queryset.
        all(): Returns all objects excluding those with status=False.
        filter(*args, **kwargs): Filters objects based on given conditions, excluding those with status=False.
        count(): Returns the count of objects excluding those with status=False.
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
