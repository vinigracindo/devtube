from django.test import TestCase
from django.contrib.auth import get_user_model

from model_mommy import mommy

from devtube.core.models import Course


class CourseModelTest(TestCase):
    def setUp(self):
        user = mommy.make(get_user_model())

        self.course = Course.objects.create(
            icon='django.png',
            name='Django 3 - Web development',
            description='Build three complete websites, learn back and front-end web development, and publish your site online with DigitalOcean',
            owner=user,
        )

    def test_create(self):
        self.assertTrue(Course.objects.exists())

    def test_str(self):
        self.assertEqual('Django 3 - Web development', str(self.course))

    def test_description_can_be_blank(self):
        field = Course._meta.get_field('description')
        self.assertTrue(field.blank)