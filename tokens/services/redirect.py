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
    
    Token.objects.filter(pk=token.pk).update(requests_count=F("requests_count")+1)
    return getattr(token, 'full_url')


def redirection(request, short_url: str):
    try:
        full_url = get_full_url(short_url)
        return redirect(full_url)
    except Exception as e:
        return HttpResponse(e.args)