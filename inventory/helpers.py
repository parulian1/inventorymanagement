from django.http import HttpRequest
from rest_framework.reverse import reverse
from rest_framework.request import Request
from urllib.parse import urlencode


def get_full_url(viewname, query_params=None, request=None, *args, **kwargs):
    """
    Reverses a URL with optional query parameters and returns the full URL,
    including the scheme and host.
    """
    if request is None:
         # Create a dummy request if one is not provided (for use outside views)
        request = Request(HttpRequest())

    base_url = reverse(viewname, request=request, args=args, kwargs=kwargs)

    if query_params:
        encoded_params = urlencode(query_params)
        return f"{base_url}?{encoded_params}"
    return base_url