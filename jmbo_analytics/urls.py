from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(
        r'^google-analytics/$', 
        'jmbo_analytics.views.google_analytics.google_analytics', 
        {}, 
        'google-analytics'
    ),
)
