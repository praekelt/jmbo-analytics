import time
import httplib2
import re
import struct

from django.http import HttpResponse
from django.views.decorators.cache import never_cache

from jmboanalytics.utils import build_ga_params


GIF_DATA = reduce(lambda x, y: x + struct.pack('B', y),
                  [0x47, 0x49, 0x46, 0x38, 0x39, 0x61,
                   0x01, 0x00, 0x01, 0x00, 0x80, 0x00,
                   0x00, 0x00, 0x00, 0x00, 0xff, 0xff,
                   0xff, 0x21, 0xf9, 0x04, 0x01, 0x00,
                   0x00, 0x00, 0x00, 0x2c, 0x00, 0x00,
                   0x00, 0x00, 0x01, 0x00, 0x01, 0x00,
                   0x00, 0x02, 0x01, 0x44, 0x00, 0x3b], '')


def get_ip(remote_address):
    if not remote_address:
        return ''
    matches = re.match('^([^.]+\.[^.]+\.[^.]+\.).*', remote_address)
    if matches:
        return matches.groups()[0] + "0"
    else:
        return ''


def google_analytics_request(request, response, path=None, event=None):
    params = build_ga_params(request)

    COOKIE_USER_PERSISTENCE = params.get('COOKIE_USER_PERSISTENCE')
    COOKIE_NAME = params.get('COOKIE_NAME')
    COOKIE_PATH = params.get('COOKIE_PATH')
    utm_url = params.get('utm_url')
    visitor_id = params.get('visitor_id')
    user_agent = params.get('user_agent')
    language = params.get('language')

    time_tup = time.localtime(time.time() + COOKIE_USER_PERSISTENCE)

    # always try and add the cookie to the response
    response.set_cookie(
        COOKIE_NAME,
        value=visitor_id,
        expires=time.strftime('%a, %d-%b-%Y %H:%M:%S %Z', time_tup),
        path=COOKIE_PATH,
    )

    # send the request
    http = httplib2.Http()
    try:
        resp, content = http.request(
            utm_url, 'GET',
            headers={
                'User-Agent': user_agent,
                'Accepts-Language:': language
            }
        )
        # send debug headers if debug mode is set
        if request.GET.get('utmdebug', False):
            response['X-GA-MOBILE-URL'] = utm_url
            response['X-GA-RESPONSE'] = resp

        # return the augmented response
        return response
    except httplib2.HttpLib2Error:
        raise Exception("Error opening: %s" % utm_url)


@never_cache
def google_analytics(request):
    """Image that sends data to Google Analytics."""
    event = request.GET.get('event', None)
    if event:
        event = event.split(',')
    response = HttpResponse('', 'image/gif', 200)
    response.write(GIF_DATA)
    return google_analytics_request(request, response, event=event)
