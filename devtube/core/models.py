from django.db import models
from django.conf import settings


class Course(models.Model):
    icon = models.ImageField(upload_to='icons/')
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name