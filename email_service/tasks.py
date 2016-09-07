from time import sleep
from django.core.mail import EmailMessage
from golden_mail.celery import app


@app.task
def send_email(message, addressee):
    email = EmailMessage('Golden Mail', message, to=[addressee])
    email.send()