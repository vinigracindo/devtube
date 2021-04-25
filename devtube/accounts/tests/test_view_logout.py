from django.test import TestCase, Client

from django.contrib.auth import  get_user_model
from django.shortcuts import resolve_url as r


class LogoutGet(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user('username', 'email@mail.com', 'password')
        self.client.login(username=self.user.username, password='password')
        self.response = self.client.get(r('accounts:logout'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_logout(self):
        session = self.response.wsgi_request.session
        self.assertNotIn('_auth_user_id', session)
