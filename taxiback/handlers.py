from rest_framework.views import exception_handler
from django.http import Http404


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if hasattr(exc, 'errors_data'):
        response.data['errors'] = exc.errors_data

    return response