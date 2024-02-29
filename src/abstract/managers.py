from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def all(self):
        return super().all().exclude(status=True)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs).exclude(status=False)

    def count(self):
        return self.filter().count()
