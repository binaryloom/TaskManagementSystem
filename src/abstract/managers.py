from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def filter(self, *args, **kwargs):
        return (
            super()
            .filter(*args, **kwargs, created_by=self.model.operating_user)
            .exclude(status=False)
        )

    def all(self):
        print(self.model)
        return super().filter()

    def count(self):
        return self.all().count()
