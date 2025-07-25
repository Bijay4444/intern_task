from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Course, CourseLog


@receiver(post_save, sender=Course)
def log_course_save(sender, instance, created, **kwargs):
    """
    Signal handler to automatically log when a course is created or updated.
    """
    if created:
        CourseLog.objects.create(
            course=instance,
            action='created',
            details=f'Course "{instance.title}" was created'
        )
    else:
        CourseLog.objects.create(
            course=instance,
            action='updated',
            details=f'Course "{instance.title}" was updated'
        )
