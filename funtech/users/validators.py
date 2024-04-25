import re

from django.core.exceptions import ValidationError

INVALID_MOBILE_NUMBER_ERROR_TEXT = 'номер телефона не соответствует формату: \
                                    +* *** *** ** **'


def mobile_number_validator(value):
    if not re.match(r'^\+\d\ [\d]{3}\ [\d]{3}\ [\d]{2}\ [\d]{2}$', value):
        raise ValidationError(INVALID_MOBILE_NUMBER_ERROR_TEXT)
    return value
