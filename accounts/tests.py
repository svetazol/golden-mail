from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestRegister(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register(self):
        self.assertEqual(len(User.objects.all()), 0)
        response = self.client.post(reverse('accounts:register'),
                                    {'username': 'foo',
                                     'password1': '12345678bar',
                                     'password2': '12345678bar'})
        self.assertEqual(response.status_code, 302)
        users = User.objects.all()
        self.assertEqual(len(users), 1)
        self.assertTrue(users[0].is_authenticated(), True)