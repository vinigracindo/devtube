from django.shortcuts import render
from django.views.generic import DetailView

from devtube.core.models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'core/index.html', {'courses': courses})


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'core/course/detail.html'
