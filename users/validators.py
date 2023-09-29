import re
from django.core.exceptions import ValidationError


class PasswordValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('^[a-zA-Z0-9]+$')
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('Пароль должен содержать только латинские буквы и цифры')

# def validate_password(field):
#     pattern = r'^[a-zA-Z0-9]*$'
#     if not re.match(r'[a-zA-Z0-9]', str(field)):
#         raise ValidationError('Пароль должен содержать только латинские буквы и цифры')
#     if 6 <= len(field) <= 12:
#         raise ValidationError('Пароль должен содержать не менее 6 символов и не более 12')
