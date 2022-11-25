from rest_framework.views import exception_handler

from django_telemetry.actions import handle_exception

def telemetry_exception_handler(exception, context):
    
    response = handle_exception(exception=exception,request=context)

    return response