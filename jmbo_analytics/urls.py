from django.conf.urls.defaults import *


urlpatterns = patterns('jmbo.analytics.views.ga',
    url(r'^ga/$', 'ga', {}, 'ga'),
)
