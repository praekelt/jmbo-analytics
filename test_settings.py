DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jmbo',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'jmbo_analytics',
    'djcelery'
)

ROOT_URLCONF = 'jmbo_analytics.urls'

# Disable celery
CELERY_ALWAYS_EAGER = True
BROKER_BACKEND = 'memory'

JMBO_ANALYTICS = {
    "google_analytics_id": "xxx"
}
