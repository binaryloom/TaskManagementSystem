from django import forms
from django.db.models import ForeignKey


class ModelForm(forms.ModelForm):
    exclude_models = ["user.User"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self._meta.model._meta.get_fields():
            if (
                isinstance(field, ForeignKey)
                and f"{field.related_model._meta.app_label}.{field.related_model._meta.object_name}"
                not in self.exclude_models
            ):
                self.fields[field.name].queryset = self.fields[
                    field.name
                ].queryset.filter(created_by=kwargs.pop("user", None))

    class Meta:
        exclude = ["status", "created_by", "updated_by"]
