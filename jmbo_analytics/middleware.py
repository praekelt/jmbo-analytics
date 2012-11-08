from jmbo_analytics.utils import build_ga_params
from jmbo_analytics.tasks import send_ga_tracking
from django.conf import settings


class GoogleAnalyticsMiddleware(object):
    def process_request(self, request):
        if hasattr(settings, 'GOOGLE_ANALYTICS_IGNORE_PATH'):
            exclude = [p for p in settings.GOOGLE_ANALYTICS_IGNORE_PATH\
                        if request.path.startswith(p)]
            if any(exclude):
                return

        path = request.path
        referer = request.META.get('HTTP_REFERER', '')
        params = build_ga_params(request, path=path, referer=referer)
        send_ga_tracking.delay(params)
