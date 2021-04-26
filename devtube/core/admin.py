from django.contrib import admin

from devtube.core.models import Course, Video

# Register your models here.
admin.site.register(Course)
admin.site.register(Video)