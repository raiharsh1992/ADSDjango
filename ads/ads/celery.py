import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ads.settings')

app = Celery('ads')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(settings.INSTALLED_APPS)