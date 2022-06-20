import os
from datetime import timedelta
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demos.settings')


#demos is our project name
app = Celery('demos')


# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "runs_every_minutes": {
        "task": "tasks.tasks.download_a_cat", #task to be triggered to worker
        "schedule": timedelta(seconds=60), #to trigger time to run onto
    },
}

