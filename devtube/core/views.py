from django.shortcuts import render
from django.views.generic import DetailView

from devtube.core.models import Course, Video


def index(request):
    courses = Course.objects.all()
    return render(request, 'core/index.html', {'courses': courses})


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'core/course/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        video_id = self.request.GET.get('video', None)
        
        if video_id:
            context['video'] = Video.objects.get(id=video_id)
        else:
            course = context['course']
            context['video'] = course.video_set.first()
       
        return context
