from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import Student


def valid_email_domains(value):
    valid_domains = ['@gmail.com', '@yahoo.com']
    for domain in valid_domains:
        if domain in value:
            break
    else:
        raise ValidationError(f'Email {value} is incorrect address')


def validate_unique_email(value):
    students = Student.object.all()

    for student in students:
        if value == student.email:
            raise ValidationError(f'Email address {value} is busy')
            break


@deconstructible
class ValidEmailDomain:
    def __init__(self, *domains):
        self.domains = list(domains)

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if args[0].endswith(domain):
                break
        else:
            raise ValidationError(f'Invalid email address. The domain <{args[0].split("@")[1]}> not valid.')
