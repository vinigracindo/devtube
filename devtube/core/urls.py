from django.urls import path

from devtube.core.views import CourseDetailView

app_name = 'core'

urlpatterns = [
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
]
