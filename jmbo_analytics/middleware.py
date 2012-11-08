from jmbo_analytics.utils import build_ga_params
from jmbo_analytics.tasks import send_ga_tracking


class GoogleAnalyticsMiddleware(object):
    def process_request(self, request):
        path = request.path
        referer = request.META.get('HTTP_REFERER', '')
        params = build_ga_params(request, path=path, referer=referer)
        send_ga_tracking.delay(params)
