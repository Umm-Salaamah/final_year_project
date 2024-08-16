# vuln_scanner_project/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vuln_scanner_project.settings')

app = Celery('vuln_scanner_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

from celery.schedules import crontab

app.conf.beat_schedule = {
    'perform-scheduled-scans': {
        'task': 'scanner.tasks.perform_scheduled_scan',
        'schedule': crontab(minute=0, hour='*/1'),  # Run every hour
    },
}

app.conf.timezone = 'UTC'
