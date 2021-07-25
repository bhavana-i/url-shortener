'''
This module contains utility functions for the urlreduce app
'''

from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 6)

AVAILABLE_CHARS = ascii_letters + digits

def create_random_code(chars=AVAILABLE_CHARS):
    """
    Creates a random string of length SIZE
    """
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )


def create_shortened_url(model_instance):
    """
    Ensures random code is unique
    """
    

    random_code = create_random_code()
    curr_long_url = model_instance.long_url

    #get the model class
    model_class = model_instance.__class__

    

    if model_class.objects.filter(short_url=random_code).exists():
        #rerun the function
        return create_shortened_url(model_instance)
    
    return random_code