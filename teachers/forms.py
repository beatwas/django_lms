from django import forms

from .models import Teacher


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        pass

    def clean_birthday(self):
        value = self.cleaned_data.get('birthday')

        return value


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthday',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
