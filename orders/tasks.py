from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
    A task that sends a notification via email after 
    the successful creation of an order object.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order no. {}'.format(order_id)
    message = 'Hello, {}! \n\n You have placed an order with us.\
    The order ID is {}'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent
