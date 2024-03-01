from django import forms


class ModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        print("-----------------------------------------")
        print(user)
        print(self._meta.model)

        fields = self._meta.model._meta.get_fields()

        for field in fields:
            if field.is_relation and field.many_to_one:
                print(field.name)
        super().__init__(*args, **kwargs)
        # if user is not None:
        #     self.fields['user'].queryset = Book.objects.filter(user=user)

    class Meta:
        exclude = ["status", "created_by", "updated_by"]
