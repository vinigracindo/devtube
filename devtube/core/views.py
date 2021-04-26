from django.shortcuts import render

from devtube.core.models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'core/index.html', {'courses': courses})
