from django.http import HttpResponse
from django.shortcuts import redirect
from tokens.models.tokens import Token
from django.db.models import F



def get_full_url(url: str):
    try:
        token = Token.objects.get(short_url__exact=url)
        if not token.is_active:
            raise KeyError(
                'Token is not available now :('
            )
    except Token.DoesNotExist:
        raise KeyError('Try another url. No such urls in DB')
    
    Token.objects.filter().update(requests_count=F("requests_count")+1)
    print(getattr(token, 'full_url'))
    return getattr(token, 'full_url')


def redirection(request, short_url: str):
    print(short_url)
    try:
        full_url = get_full_url(short_url)
        return redirect(full_url)
    except Exception as e:
        print(e)
        return HttpResponse(e.args)