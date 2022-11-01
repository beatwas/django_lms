from django import forms

from .models import Group


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'date_start',
            'description',
        ]

        widgets = {
            'date_start': forms.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        pass


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'date_start',
            'description',
        ]

        widgets = {
            'date_start': forms.DateInput(attrs={'type': 'date'})
        }
