from jmboanalytics.utils import build_ga_params
from jmboanalytics.tasks import send_ga_tracking


class GoogleAnalyticsMiddleware(object):
    def process_request(self, request):
        return send_ga_tracking.delay(build_ga_params(request))
