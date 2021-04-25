from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.conf import settings

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class LoginGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('accounts:login'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'accounts/login.html')

    def test_html(self):
        """HTML must contains input tags"""
        tags = (
            ('<form', 1),
            ('name="username"', 1),
            ('type="password"', 1),
            ('type="submit"', 1),
            ('method="post"', 1)
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must contains a AuthenticationForm"""
        form = self.response.context['form']
        self.assertIsInstance(form, AuthenticationForm)
        

class LoginPostValid(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user('username', 'contact@mail.com', 'password')
        data = dict(username=user.username, password='password')
        self.response = self.client.post(r('accounts:login'), data)

    def test_user_is_authenticated(self):
        session = self.response.wsgi_request.session
        self.assertIn('_auth_user_id', session)


class LoginPostInvalidUser(TestCase):
    def setUp(self):
        data = dict(username='username', password='wrong password')
        self.response = self.client.post(r('accounts:login'), data)

    def test_invalid_user_post(self):
        """Invalid Post should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_user_is_not_authenticated(self):
        session = self.response.wsgi_request.session
        self.assertNotIn('_auth_user_id', session)

    def test_html(self):
        """HTML must contains message errors"""
        form = self.response.context['form']
        errors = form.non_field_errors()

        for error in errors:
            with self.subTest():
                self.assertContains(self.response, error)
