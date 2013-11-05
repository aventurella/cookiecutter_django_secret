from .random import get_random_string


def random_string():
    '''
    This is lifted from the django source
    https://github.com/django/django/blob/86f4459f9e3c035ec96578617605e93234bf2700/django/core/management/commands/startproject.py#L27-L29
    '''
    # Create a random SECRET_KEY hash to put it in the main settings.
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(50, chars)
