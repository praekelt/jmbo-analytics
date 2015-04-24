Jmbo Analytics
==============
**Jmbo analytics brings the power of Google Analytics to your Django projects**

.. figure:: https://travis-ci.org/praekelt/jmbo-analytics.svg?branch=develop
   :align: center
   :alt: Travis

.. contents:: Contents
    :depth: 3

Required
--------

* You have to add ``jmbo_analytics`` to you ``INSTALLED_APPS``
* You have to specify a Google Analytics `tracking code <https://support.google.com/analytics/bin/answer.py?hl=en&answer=1008080>`_.

where ``xxx`` is your tracking code::

 JMBO_ANALYTICS = {
    'google_analytics_id': 'xxx',
 }


Usage
-----

``jmbo-analytics`` offers you two ways to add tracking to your pages.

1. HTML tag
***********

Using ``<img />`` and putting it in your ``base.html``::

 {% load jmbo_analytics_tags %}
 <div style="display: none;">
    <img src="{% google_analytics %}" width="0" height="0" />
 </div>

2. Middleware and Celery
************************

Using Django's middleware you can process every request and use Celery to make the request to Google Analytics.
Note that this does not work behind a reverse caching proxy::

 MIDDLEWARE_CLASSES = (
    'jmbo_analytics.middleware.GoogleAnalyticsMiddleware',
 )

You may have to add ``jmbo_analytics`` to your ``CELERY_IMPORTS``::

 CELERY_IMPORTS = ('jmbo_analytics.tasks')

You may also specify paths that will be excluded when tracking::

 GOOGLE_ANALYTICS_IGNORE_PATH = ['/health/', ]
