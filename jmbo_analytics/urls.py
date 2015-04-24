from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(
        r'^google-analytics/$',
        'jmbo_analytics.views.google_analytics.google_analytics',
        {},
        'google-analytics'
    ),
)
