from datetime import datetime
from unittest import mock
from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse


class TestEmailService(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post(self):
        with mock.patch('celery.CELERY_ALWAYS_EAGER', True, create=True):
            response = self.client.post(reverse('email_service:email_requests'),
                                        {'message': 'test_message',
                                         'email': 'svests@yandex.ru',
                                         'send_dttm': datetime.now()})
            self.assertEqual(response.status_code, 201)