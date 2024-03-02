from django import forms
from django.db.models import ForeignKey


class ModelForm(forms.ModelForm):
    """
    A customized ModelForm class that filters ForeignKey queryset based on the operating user.

    Attributes:
        exclude_models (list): A list of model names to exclude from ForeignKey queryset filtering.
    """

    exclude_models = ["user.User"]

    def __init__(self, *args, **kwargs):
        """
        Initialize the ModelForm instance.

        Args:
            operating_user (object): The user object for whom the queryset needs to be filtered.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        operating_user = kwargs.pop("operating_user", None)
        super().__init__(*args, **kwargs)
        for field in self._meta.model._meta.get_fields():
            if (
                isinstance(field, ForeignKey)
                and f"{field.related_model._meta.app_label}.{field.related_model._meta.object_name}"
                not in self.exclude_models
            ):
                self.fields[field.name].queryset = self.fields[
                    field.name
                ].queryset.filter(created_by=operating_user)

    class Meta:
        """
        Meta class to specify metadata options for the ModelForm.
        """

        exclude = ["status", "created_by", "updated_by"]
