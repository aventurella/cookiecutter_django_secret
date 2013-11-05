from cookiecutter.plugins import JinjaSimpleTag
from .utils import random_string


class DjangoSecret(JinjaSimpleTag):
    tags = set(['django_secret'])

    def tag_action(self, caller):
        return random_string()
