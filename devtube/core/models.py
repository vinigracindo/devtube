from django.db import models
from django.conf import settings


class Course(models.Model):
    icon = models.ImageField(upload_to='icons/')
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
    