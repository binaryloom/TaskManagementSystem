from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    # def create(self, **kwargs):
    #     # operating_user = (
    #     #     self.model.operating_user if hasattr(self.model, 'operating_user') else None
    #     # )
    #     return super().create(**kwargs)

    # def update(self, **kwargs):
    #     operating_user = (
    #         self.model.operating_user if hasattr(self.model, 'operating_user') else None
    #     )
    #     return super().update(**kwargs)

    def get_operating_user(self):
        return self.model.operating_user or get_anonymous_user()

    def console_create(self, **kwargs):
        if not self.model.operating_user:
            self.model.operating_user = self.get_operating_user()
        return super().create(**kwargs)

    def all(self):
        return super().all().exclude(status=False)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs).exclude(status=False)

    def count(self):
        return self.filter().count()

    # TOD: GET AND COUNT ARE NOT WORKING
    # DELETE IS ALSO NOT WORKING
