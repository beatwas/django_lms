from datetime import date

from django.core.validators import MinLengthValidator
from django.db import models


class Groups(models.Model):
    group_name = models.CharField(
        max_length=100,
        verbose_name='group name',
        db_column='group_name',
        validators=[MinLengthValidator(2, '"group_name" field value less than two symbols')]
    )
    date_start = models.DateField(default=date.today, null=True, blank=True)
    description = models.TextField(
        max_length=300,
        verbose_name='description',
        db_column='description',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"description" field value less than two symbols'}
    )

    def __str__(self):
        return f'{self.group_name} {self.date_start}\n{self.description}'
