from rest_framework import serializers
from .models import Course, Lesson, CourseLog


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructor',
                  'created_at', 'updated_at', 'is_active']


class LessonSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content', 'course',
                  'course_title', 'order', 'created_at', 'updated_at']


class CourseLogSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = CourseLog
        fields = ['id', 'course', 'course_title',
                  'action', 'timestamp', 'details']
