from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from .models import Course, Lesson, CourseLog
from .serializers import CourseSerializer, LessonSerializer, CourseLogSerializer


class LessonPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


class LessonListCreateAPIView(generics.ListCreateAPIView):
    """
    API view that supports search by title and paginates the result (5 per page).
    Use Django REST Framework's SearchFilter and PageNumberPagination.

    Search by adding ?search=<query> to the URL
    Navigate pages with ?page=<page_number>
    Also supports POST to create new lessons.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']  # Search by lesson title
    pagination_class = LessonPagination


class CourseListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to list all courses or create a new course.
    Creating a course will trigger the post_save signal.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a course.
    Updating a course will trigger the post_save signal.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseLogListAPIView(generics.ListAPIView):
    """
    API view to list all course logs (created automatically via signals).
    """
    queryset = CourseLog.objects.all()
    serializer_class = CourseLogSerializer
