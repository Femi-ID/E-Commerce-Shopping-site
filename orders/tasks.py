"""Celery will look for a tasks.py file in each application directory of applications added to INSTALLED_APPS
 in order to load asynchronous tasks defined in it."""

'''Use asynchronous tasks not only for time-consuming processes, but also for other processes that do not take so much time to be
executed but which are subject to connection failures or require a retry policy.'''

from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """Task to send an e-mail notification when an order is successfully created."""
    order = Order.objects.get(id=order_id)
    subject = f'Order number: {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}'
    mail_sent = send_mail(subject, message, 'femi@mail.com', [order.email])

    return mail_sent
    # send_mail(subject, message, sender, [to])


