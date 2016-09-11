from django.core.mail import EmailMessage
from email_service.models import EmailRequest
from golden_mail.celery import app


@app.task
def send_email(message, addressee, email_request_pk):
    email_request = EmailRequest.objects.get(pk=email_request_pk)
    email = EmailMessage('Golden Mail', message, to=[addressee])
    try:
        email.send()
    except Exception as e:
        # fixme: is it ok to handle errors in such way?
        email_request.status = 'внутрення_ошибка'
        raise e
    else:
        email_request.status = 'отправлено'
    finally:
        email_request.save()