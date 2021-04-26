from django.test import TestCase
from django.shortcuts import resolve_url as r

from devtube.core.models import Course

from model_mommy import mommy


class CourseDetailTest(TestCase):
    def setUp(self):
        course = mommy.make(Course)
        self.response = self.client.get(r('core:course_detail', course.pk))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/course/detail.html')

    def test_context(self):
        course = self.response.context['course']
        self.assertTrue(course)