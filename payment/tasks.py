from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order


@shared_task
def payment_completed(order_id):
    """Task to send an e-mail notification when an order is successfully created."""
    order = Order.objects.get(id=order_id)

    # create invoice e-mail
    subject = f'My shop - EE Invoice no {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])  # creatte email object.

    # generate PDF
    html = render_to_string('order/order/pdf.html', {'order': order})  # render template
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # generate the PDF file from the template and output it to a BytesIO instance which is an in-memory bytes buffer.

    # attach PDF file
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')

    # send e-mail
    email.send()


