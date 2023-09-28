import re
from django.core.exceptions import ValidationError


def validate_password(value):
    pattern = r'^[a-zA-Z0-9]*$'
    if not re.match(pattern, value):
        raise ValidationError('Пароль должен содержать только латинские буквы и цифры')
    if 6 <= len(value) <= 12:
        raise ValidationError('Пароль должен содержать не менее 6 символов и не более 12')
