from datetime import date, time

from django.core.exceptions import ValidationError


def validate_start_date(value):
    current_date = date.today()

    try:
        if ":" in value:
            time.strptime(value, "%Y-%m-%d %H:%M:%S")
        else:
            time.strptime(value, "%Y-%m-%d")

            if value.day < current_date.day | value.month < current_date.month | value.year < current_date.year:
                raise ValidationError('Date is not valid')
    except Exception as e:
        raise ValidationError(e)
