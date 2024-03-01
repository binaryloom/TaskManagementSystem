from django import forms


class ModelForm(forms.ModelForm):

    class Meta:
        exclude = ["status", "created_by", "updated_by"]
