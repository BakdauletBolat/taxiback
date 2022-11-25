from array import array
from time import monotonic
import sys
from django.conf import settings
from django_telemetry.actions import create_web_telemetry
from django_telemetry.actions import handle_exception
from django_telemetry.tasks import try_to_string_byte


class WebTelemetryMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def get_path_array(self):
        try:
            paths = settings.TELEMETRY_URLS
        except Exception:
            paths = ['api']

        return paths

    def __call__(self, request):

        start_time = monotonic()

        raw_body = try_to_string_byte(request.body)

        response = self.get_response(request)

        paths = self.get_path_array()

        path_array = request.path.split('/')

        try:
            end_time = int((monotonic() - start_time) * 1000)
            if path_array[1] in paths:
                create_web_telemetry(request, response, end_time, raw_body)
        except Exception as e:
            print(sys.stderr, "Error saving request log", e)

        return response

    def process_exception(self, request, exception):

        response = handle_exception(exception=exception, request=request)

        return response
