# tasks.py

from celery import shared_task
from core.utils import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import smart_bytes


@shared_task
def send_password_change_email(email, code):
    message = render_to_string('password_change_email.html', {'code': code})
    encoded_message = smart_bytes(message, 'utf-8')
    send_mail(encoded_message, email, 'Смена пароля')
