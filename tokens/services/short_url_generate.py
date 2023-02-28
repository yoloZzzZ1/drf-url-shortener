import string

from random import choices


TOKEN_LENGTH=6

def generate_short_url():
    short_url = ''.join(choices(
        string.ascii_letters,
        k=TOKEN_LENGTH
    ))
    return short_url