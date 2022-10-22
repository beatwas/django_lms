from django import forms

from .models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone',
        ]

    def clean(self):
        pass

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name').title()

        return value

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name').title()

        return value

    def clean_birthday(self):
        value = self.cleaned_data.get('birthday')

        return value

    def clean_phone(self):
        phone_number = self.cleaned_data.get('phone')
        value = ''

        for x in phone_number:
            if x in '0123456789-()':
                value += x

        return value
