from django.urls import path
from .views import (
    LessonListCreateAPIView,
    CourseListCreateAPIView,
    CourseDetailAPIView,
    CourseLogListAPIView
)

urlpatterns = [
    # Lesson endpoints
    path('lessons/', LessonListCreateAPIView.as_view(), name='lesson-list-create'),

    # Course endpoints
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),

    # Course log endpoints
    path('course-logs/', CourseLogListAPIView.as_view(), name='course-log-list'),
]
