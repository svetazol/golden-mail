from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'golden_mail.settings')

from django.conf import settings  # noqa

app = Celery('golden_mail')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

print(app.conf.CELERY_TIMEZONE)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))