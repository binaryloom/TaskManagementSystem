from django.db import models


class BaseManager(models.Manager):
    operating_user = None

    def get_queryset(self):
        return super().get_queryset()

    def filter(self, *args, **kwargs):
        operating_user = (
            self.operating_user if hasattr(self, "operating_user") else None
        )
        print("******")
        attrs_with_values = vars(self.model)
        for attr, value in attrs_with_values.items():
            print(f"{attr}: {value}")
        print("-------------")
        print(dir(self.model))

        print("5454545454565451-------------------------------------")
        print(self.model.get_operating_user(self.model))
        print("******")

        return (
            super()
            .filter(*args, **kwargs, created_by=self.model.operating_user)
            .exclude(status=False)
        )

    def all(self):
        return self.filter()

    def count(self):
        return self.all().count()
