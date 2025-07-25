from django.contrib import admin
from .models import Course, Lesson, CourseLog


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor',
                    'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'instructor']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(CourseLog)
class CourseLogAdmin(admin.ModelAdmin):
    list_display = ['course', 'action', 'timestamp']
    list_filter = ['action', 'timestamp']
    readonly_fields = ['course', 'action', 'timestamp', 'details']

    def has_add_permission(self, request):
        # Prevent manual creation of logs (they should be created via signals)
        return False

    def has_change_permission(self, request, obj=None):
        # Prevent editing of logs
        return False
