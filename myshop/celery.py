import os
from celery import Celery

# set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# The namespace attribute specifies the prefix that Celery-related settings will have in your settings.py file.
# By setting the CELERY namespace, all Celery settings need to include the
# CELERY_ prefix in their name (for example, CELERY_BROKER_URL).


# Finally, you tell Celery to auto-discover asynchronous tasks for your applications.
# Celery will look for a tasks.py file in each application directory of applications added to INSTALLED_APPS
# in order to load asynchronous tasks defined in it.

