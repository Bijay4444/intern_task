from django.urls import path
from .views import (
    LessonListAPIView,
    CourseListCreateAPIView,
    CourseDetailAPIView,
    CourseLogListAPIView
)

urlpatterns = [
    # Lesson endpoints
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),

    # Course endpoints
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),

    # Course log endpoints
    path('course-logs/', CourseLogListAPIView.as_view(), name='course-log-list'),
]
