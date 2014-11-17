import struct

from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.conf import settings

from jmbo_analytics.utils import build_ga_params, set_cookie
from jmbo_analytics.tasks import send_ga_tracking


GIF_DATA = reduce(lambda x, y: x + struct.pack('B', y),
                  [0x47, 0x49, 0x46, 0x38, 0x39, 0x61,
                   0x01, 0x00, 0x01, 0x00, 0x80, 0x00,
                   0x00, 0x00, 0x00, 0x00, 0xff, 0xff,
                   0xff, 0x21, 0xf9, 0x04, 0x01, 0x00,
                   0x00, 0x00, 0x00, 0x2c, 0x00, 0x00,
                   0x00, 0x00, 0x01, 0x00, 0x01, 0x00,
                   0x00, 0x02, 0x01, 0x44, 0x00, 0x3b], '')


@never_cache
def google_analytics(request):
    """Image that sends data to Google Analytics."""

    response = HttpResponse('', 'image/gif', 200)
    response.write(GIF_DATA)

    if hasattr(settings, 'GOOGLE_ANALYTICS_IGNORE_PATH'):
        exclude = [p for p in settings.GOOGLE_ANALYTICS_IGNORE_PATH\
                    if request.path.startswith(p)]
        if any(exclude):
            return response

    event = request.GET.get('event', None)
    if event:
        event = event.split(',')
    path = request.path
    referer = request.META.get('HTTP_REFERER', '')
    params = build_ga_params(request, path, event, referer)
    send_ga_tracking.delay(params)

    set_cookie(params, response)
    return response
