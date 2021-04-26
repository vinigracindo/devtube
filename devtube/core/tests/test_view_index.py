from django.test import TestCase
from django.shortcuts import resolve_url as r

from model_mommy import mommy

from devtube.core.models import Course


class IndexGet(TestCase):
    def setUp(self):
        self.courses = mommy.make(Course, 5)
        self.response = self.client.get(r('index'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/index.html')

    def test_context(self):
        courses = self.response.context['courses']
        self.assertEqual(len(courses), 5)