from django import forms


class ModelForm(forms.ModelForm):
    pass
    # class Meta:
    #     exclude = ["status", "created_by", "updated_by"]
