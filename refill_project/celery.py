import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'refill_project.settings')

app = Celery('refill_project')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()