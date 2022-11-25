from django.http import JsonResponse
from django_telemetry.models import WebTelemetry, WebQuery
from django.contrib.auth.models import User
from django.db import connection
import json
from django_telemetry.tasks import try_to_string_byte



def handle_exception(exception, request):
    error = {
        'status_code': 500,
        'detail': ''
    }

    if exception:
        str_type = exception.__class__.__name__
        try:
            exception_detail = exception.get_full_details()
        except Exception:
            exception_detail = str(exception)

        try:
            status_code = exception.status_code
        except Exception:
            status_code = 400

        error['status_code'] = status_code
        error['type'] = str_type
        error['detail'] = exception_detail

        return JsonResponse(error, status=error['status_code'])


def dumps(value):
    return json.dumps(value, default=lambda o: None)


def create_web_telemetry(request, response, duration_time, raw_body):
    if hasattr(request, 'user'):
        user_id = request.user.id if type(request.user) == User else None
    else:
        user_id = None

    meta = request.META.copy()
    meta.pop('QUERY_STRING', None)
    meta.pop('HTTP_COOKIE', None)
    remote_addr_fwd = None

    if 'HTTP_X_FORWARDED_FOR' in meta:
        remote_addr_fwd = meta['HTTP_X_FORWARDED_FOR'].split(",")[0].strip()
        if remote_addr_fwd == meta['HTTP_X_FORWARDED_FOR']:
            meta.pop('HTTP_X_FORWARDED_FOR')

    try:
        post = request.POST
    except Exception as e:
        post = None

    content = try_to_string_byte(response.content)

    tel = WebTelemetry.objects.using('django_telemetry').create(
        host=request.get_host(),
        path=request.path,
        headers=request.headers,
        method=request.method,
        uri=request.build_absolute_uri(),
        status_code=response.status_code,
        user_agent=meta.pop('HTTP_USER_AGENT', None),
        remote_addr=meta.pop('REMOTE_ADDR', None),
        remote_addr_fwd=remote_addr_fwd,
        meta=None if not meta else dumps(meta),
        cookies=None if not request.COOKIES else dumps(request.COOKIES),
        get=None if not request.GET else dumps(request.GET),
        post=post,
        raw_post=raw_body,
        is_secure=request.is_secure(),
        response=content,
        is_ajax=True,
        user_id=user_id,
        duration=duration_time,
    )

    for query in connection.queries:
        WebQuery.objects.using('django_telemetry').create(sql=query['sql'], time=query['time'], telemetry=tel)

    return tel
