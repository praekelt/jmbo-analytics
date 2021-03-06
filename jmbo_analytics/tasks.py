import requests
from celery.task import task


@task(ignore_result=True)
def send_ga_tracking(params):
    utm_url = params.get('utm_url')
    user_agent = params.get('user_agent')
    language = params.get('language')
    headers={
        'User-Agent': user_agent,
        'Accept-Language': language
    }
    try:
        requests.get(utm_url, headers=headers)
    except requests.HTTPError:
        pass
