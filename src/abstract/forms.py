from django import forms


class ModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        print("-----------------------------------------")
        print(user)
        print(self._meta.model)

        fields = self._meta.model._meta.get_fields()
        # task_management.Task.id
        # task_management.Task.status
        # task_management.Task.created_at
        # task_management.Task.updated_at
        # task_management.Task.created_by
        # task_management.Task.updated_by
        # task_management.Task.title
        # task_management.Task.description
        # task_management.Task.assigned_list
        # task_management.Task.due_date
        # task_management.Task.assigned_to
        for field in fields:
            print(field)
            # if field.is_relation:
            #     model_str = f"{field.related_model._meta.app_label}.{field.related_model._meta.object_name}"
            #     print("field_name", field.name)

            #     print("related model", model_str)
        super().__init__(*args, **kwargs)
        # if user is not None:
        #     self.fields['user'].queryset = Book.objects.filter(user=user)

    class Meta:
        exclude_models = ["user.User"]
        exclude = ["status", "created_by", "updated_by"]
