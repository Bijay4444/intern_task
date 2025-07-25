# API Testing Guide for Both Tasks

## Base URL: http://127.0.0.1:8080

---

## 🎯 TASK 1 TESTING: Models with Signals

### 1. Create a Course (Should trigger 'created' signal)

**Method**: POST  
**URL**: `http://127.0.0.1:8080/api/courses/`  
**Headers**: `Content-Type: application/json`  
**Body**:

```json
{
  "title": "Python Programming Basics",
  "description": "Learn Python from scratch with hands-on examples",
  "instructor": 1,
  "is_active": true
}
```

### 2. Update a Course (Should trigger 'updated' signal)

**Method**: PUT  
**URL**: `http://127.0.0.1:8080/api/courses/1/` (replace 1 with actual course ID)  
**Headers**: `Content-Type: application/json`  
**Body**:

```json
{
  "title": "Advanced Python Programming",
  "description": "Updated description for advanced Python course",
  "instructor": 1,
  "is_active": true
}
```

### 3. Check Course Logs (Verify signals worked)

**Method**: GET  
**URL**: `http://127.0.0.1:8080/api/course-logs/`  
**Expected**: Should show log entries for 'created' and 'updated' actions

### 4. List All Courses

**Method**: GET  
**URL**: `http://127.0.0.1:8080/api/courses/`

---

## 🎯 TASK 2 TESTING: Searchable and Paginated API

### First, create some lessons for testing:

### 1. Create Course for Lessons

**Method**: POST  
**URL**: `http://127.0.0.1:8080/api/courses/`  
**Body**:

```json
{
  "title": "Web Development Course",
  "description": "Full stack web development",
  "instructor": 1,
  "is_active": true
}
```

### 2. Create Multiple Lessons (Create these one by one)

**Method**: POST  
**URL**: `http://127.0.0.1:8080/api/lessons/` (if you have this endpoint, or use Django admin)

**Lesson 1**:

```json
{
  "title": "Python Basics",
  "content": "Introduction to Python programming",
  "course": 1,
  "order": 1
}
```

**Lesson 2**:

```json
{
  "title": "JavaScript Fundamentals",
  "content": "Learn JavaScript basics",
  "course": 1,
  "order": 2
}
```

**Lesson 3**:

```json
{
  "title": "Python Advanced Topics",
  "content": "Advanced Python concepts",
  "course": 1,
  "order": 3
}
```

**Lesson 4**:

```json
{
  "title": "HTML and CSS",
  "content": "Web markup and styling",
  "course": 1,
  "order": 4
}
```

**Lesson 5**:

```json
{
  "title": "Python Web Frameworks",
  "content": "Django and Flask",
  "course": 1,
  "order": 5
}
```

**Lesson 6**:

```json
{
  "title": "Database Design",
  "content": "SQL and database concepts",
  "course": 1,
  "order": 6
}
```

### Now Test the Main Requirement:

### 3. Test Pagination (5 per page)

**Method**: GET  
**URL**: `http://127.0.0.1:8080/api/lessons/`  
**Expected**: Should return max 5 lessons with pagination info

### 4. Test Pagination - Page 2

**Method**: GET  
**URL**: `http://127.0.0.1:8080/api/lessons/?page=2`  
**Expected**: Should return remaining lessons

### 5. Test Search by Title - "Python"

**Method**: GET  
**URL**: `http://127.0.0.1:8080/api/lessons/?search=python`  
**Expected**: Should return only lessons with "python" in title

### 6. Test Search by Title - "JavaScript"

**Method**: GET  
**URL**: `http://127.0.0.1:8080/api/lessons/?search=javascript`  
**Expected**: Should return only JavaScript related lessons

### 7. Test Search with Pagination

**Method**: GET  
**URL**: `http://127.0.0.1:8080/api/lessons/?search=python&page=1`  
**Expected**: Should return paginated results for Python lessons

---

## 🧪 VERIFICATION CHECKLIST

### ✅ Task 1 - Signals Working:

- [ ] Creating course shows in course-logs with action='created'
- [ ] Updating course shows in course-logs with action='updated'
- [ ] Timestamps are automatically added
- [ ] Course logs cannot be manually created (admin should prevent this)

### ✅ Task 2 - API Features Working:

- [ ] GET /api/lessons/ returns paginated results (5 per page)
- [ ] Search parameter ?search=python filters by title
- [ ] Pagination ?page=2 works correctly
- [ ] Combined search and pagination works
- [ ] Response includes pagination metadata (next, previous, count)

---

## 📝 EXPECTED RESPONSE FORMATS

### Course Creation Response:

```json
{
  "id": 1,
  "title": "Python Programming Basics",
  "description": "Learn Python from scratch",
  "instructor": 1,
  "created_at": "2025-01-XX...",
  "updated_at": "2025-01-XX...",
  "is_active": true
}
```

### Course Logs Response:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 2,
      "course": 1,
      "course_title": "Advanced Python Programming",
      "action": "updated",
      "timestamp": "2025-01-XX...",
      "details": "Course \"Advanced Python Programming\" was updated"
    },
    {
      "id": 1,
      "course": 1,
      "course_title": "Python Programming Basics",
      "action": "created",
      "timestamp": "2025-01-XX...",
      "details": "Course \"Python Programming Basics\" was created"
    }
  ]
}
```

### Lessons with Pagination Response:

```json
{
  "count": 6,
  "next": "http://127.0.0.1:8080/api/lessons/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Python Basics",
      "content": "Introduction to Python programming",
      "course": 1,
      "course_title": "Web Development Course",
      "order": 1,
      "created_at": "2025-01-XX...",
      "updated_at": "2025-01-XX..."
    }
    // ... 4 more lessons
  ]
}
```

---

## 🚀 Quick Terminal Test Commands

```bash
# Test Course Creation (Task 1)
curl -X POST http://127.0.0.1:8080/api/courses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Course", "description": "Test", "instructor": 1}'

# Check Course Logs (Task 1)
curl http://127.0.0.1:8080/api/course-logs/

# Test Lesson Pagination (Task 2)
curl http://127.0.0.1:8080/api/lessons/

# Test Lesson Search (Task 2)
curl "http://127.0.0.1:8080/api/lessons/?search=python"
```
