from django.http import HttpResponse
from django.conf import settings


def token_required(view):
    def wrapper(request, *args, **kwargs):
        if 'HTTP_X_AUTH_TOKEN' not in request.META:
            return HttpResponse('{"message":"Missing token header"}', status=403)
        if request.META.get('HTTP_X_AUTH_TOKEN') != settings.AUTH_TOKEN:
            return HttpResponse('{"message":"Not authorized"}', status=403)
        return view(request, *args, **kwargs)
    return wrapper