from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def filter(self, *args, **kwargs):
        print("******")
        print(self.model.operating_user)
        print("******")
        print("this is filter method", self.model.operating_user)
        return (
            super()
            .filter(*args, **kwargs, created_by=self.model.operating_user)
            .exclude(status=False)
        )

    def all(self):
        print(self.model)
        print("---------------------------")

        return self.filter()

    def count(self):
        return self.all().count()
