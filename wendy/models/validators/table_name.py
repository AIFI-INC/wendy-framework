from tortoise.validators import Validator
from tortoise.exceptions import ValidationError
from typing import Any


class TableNameValidator(Validator):
    def __call__(self, value: Any):
        # TODO: append some validations
        return super().__call__(value)
