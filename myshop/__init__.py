"""Importing celery module here to make sure it is loaded when Django starts."""

# import celery
from .celery import app as celery_app


'''CELERY_ALWAYS_EAGER setting allows you to execute tasks locally in a synchronous way, instead of sending them to the queue.
This is useful for running unit tests or executing the application in your local environment without running Celery.'''
