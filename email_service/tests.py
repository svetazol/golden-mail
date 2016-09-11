from datetime import datetime
from unittest import mock

from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from django.test import override_settings
from django.urls import reverse

from email_service.models import EmailRequest


class TestEmailService(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='test')

    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory',
                       EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
    def test_post(self):
        # with mock.patch('golden_mail.celery.app.conf.CELERY_ALWAYS_EAGER', True, create=True):
            is_success_login = self.client.login(username='test', password='test')
            self.assertEqual(is_success_login, True)
            response = self.client.post(reverse('email_service:email_requests'),
                                        {'message': 'test_message',
                                         'email': 'svests@yandex.ru',
                                         'sending_dttm': datetime.now() })
            self.assertEqual(response.status_code, 201)
            email_request = EmailRequest.objects.get(pk=response.data.get('id'))
            self.assertEqual(email_request.status , 'отправлено')
