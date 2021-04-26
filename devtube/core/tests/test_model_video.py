from django.test import TestCase

from model_mommy import mommy

from devtube.core.models import Course, Video


class VideoModelTest(TestCase):
    def setUp(self):
        course = mommy.make(Course)

        self.video = Video.objects.create(
            course=course,
            title='Hello',
            content='video/hello.mp4',
        )

    def test_create(self):
        self.assertTrue(Video.objects.exists())

    def test_str(self):
        self.assertEqual('Hello', str(self.video))