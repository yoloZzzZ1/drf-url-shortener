import string

from random import choices
from tokens.models.tokens import Token


TOKEN_LENGTH=6

def generate_short_url():
    while True:
        
        short_url = ''.join(choices(
            string.ascii_letters,
            k=TOKEN_LENGTH
        ))

        if not Token.objects.filter(
            short_url=short_url
        ).exists():
            break

    return short_url