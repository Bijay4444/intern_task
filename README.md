# Django Interview Task Implementation

This project implements two key tasks for the internship interview:

## Task 1: Model with Signals ✅

**Objective**: Create a Course model and CourseLog model. Use post_save signal to automatically log when a course is created or updated.

### Implementation:

- **Course Model**: Contains title, description, instructor, timestamps, and active status
- **CourseLog Model**: Automatically tracks course creation and updates
- **Signals**: `post_save` signal automatically creates log entries
- **Additional**: Added Lesson model for the API task

### Models Created:

```python
# Course model with basic fields
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

# CourseLog model for automatic logging
class CourseLog(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='logs')
    action = models.CharField(max_length=10, choices=[('created', 'Created'), ('updated', 'Updated')])
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)
```

### Signal Implementation:

```python
@receiver(post_save, sender=Course)
def log_course_save(sender, instance, created, **kwargs):
    if created:
        CourseLog.objects.create(course=instance, action='created', ...)
    else:
        CourseLog.objects.create(course=instance, action='updated', ...)
```

## Task 2: Searchable and Paginated API ✅

**Objective**: Build a LessonListAPIView that supports search by title and paginates the result (5 per page). Use Django REST Framework's SearchFilter and PageNumberPagination.

### Implementation:

- **LessonListAPIView**: Supports search by title
- **Pagination**: 5 items per page using PageNumberPagination
- **Search**: Uses Django REST Framework's SearchFilter
- **Additional APIs**: Full CRUD for courses and course logs viewing

### API Endpoints:

#### Lesson API (Main Requirement)

- `GET /api/lessons/` - List lessons with search and pagination
- `GET /api/lessons/?search=python` - Search lessons by title
- `GET /api/lessons/?page=2` - Navigate to page 2

#### Additional APIs

- `GET /api/courses/` - List all courses
- `POST /api/courses/` - Create new course (triggers signal)
- `GET /api/courses/{id}/` - Get specific course
- `PUT /api/courses/{id}/` - Update course (triggers signal)
- `DELETE /api/courses/{id}/` - Delete course
- `GET /api/course-logs/` - View all course logs (created by signals)

## Installation & Setup

### Dependencies

```bash
# Install dependencies
pip install -r requirements.txt
```

### Database Setup

```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

## Testing the Implementation

### 1. Test Signals (Task 1)

1. Access admin panel: http://127.0.0.1:8000/admin/
2. Create a new Course
3. Check CourseLog to see automatic log entry
4. Update the Course
5. Verify another log entry was created

### 2. Test API (Task 2)

```bash
# List lessons with pagination (5 per page)
curl http://127.0.0.1:8000/api/lessons/

# Search lessons by title
curl http://127.0.0.1:8000/api/lessons/?search=python

# Navigate to page 2
curl http://127.0.0.1:8000/api/lessons/?page=2

# Create a course (will trigger signal)
curl -X POST http://127.0.0.1:8000/api/courses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Course", "description": "Test", "instructor": 1}'
```

## Features Implemented

### ✅ Task 1 Features:

- [x] Course model with proper fields
- [x] CourseLog model for tracking changes
- [x] post_save signal implementation
- [x] Automatic logging on create/update
- [x] Admin interface for testing

### ✅ Task 2 Features:

- [x] LessonListAPIView with pagination
- [x] Search by title functionality
- [x] 5 items per page pagination
- [x] Django REST Framework SearchFilter
- [x] PageNumberPagination implementation

### 🎯 Bonus Features:

- [x] Complete CRUD API for courses
- [x] CourseLog viewing API
- [x] Proper serializers for all models
- [x] Admin interface with readonly logs
- [x] Comprehensive URL routing
- [x] Requirements.txt for dependencies

## Project Structure

```
merocodingtask/
├── courses/
│   ├── models.py          # Course, Lesson, CourseLog models
│   ├── signals.py         # post_save signal handlers
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views with search & pagination
│   ├── urls.py            # URL routing
│   └── admin.py           # Admin interface
├── merocodingtask/
│   ├── settings.py        # Django + DRF configuration
│   └── urls.py            # Main URL configuration
└── requirements.txt       # Project dependencies
```

## Key Technologies Used

- Django 5.2.4
- Django REST Framework 3.16.0
- Django Signals
- SQLite (default database)

Both tasks have been successfully implemented with additional bonus features for a complete API solution!
