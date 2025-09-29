# Research Portal - Task Management System

A Django-based Task Management System that allows users to manage and track tasks efficiently. This project is designed to handle a large number of users and tasks while providing a responsive and user-friendly frontend.

---

## **Features**

### **Users**
- User registration and login (Django authentication)
- Each user has:
  - `user_id`
  - `name`
  - `email`
  - `registration_date`
- A user can have multiple tasks assigned

### **Tasks**
- Each task has:
  - `task_id`
  - `title`
  - `description`
  - `assigned_user`
  - `status` (pending, in-progress, completed)
  - `priority` (low, medium, high)
  - `due_date`
  - `created_at`
- Tasks can be filtered by status, priority, and due date (in admin)
- Pagination for large task lists
- Atomic updates and indexed fields for performance

### **Frontend**
- Task dashboard with a clean, responsive Bootstrap design
- Color-coded badges for task status and priority
- Pagination support
- Task list page showing assigned user, status, priority, and due date

### **Backend & API**
- Django REST Framework for API endpoints
- REST API for Users and Tasks
- CRUD support via API
- Search and filtering support
- Transaction integrity with atomic updates

### **Performance Considerations**
- Indexed fields: `assigned_user`, `status`, `due_date`
- Pagination for large datasets
- Designed to scale for 100k+ users and 1M+ tasks

---

## **Installation**

1. Clone the repository:

```bash
git clone <your-repo-url>
cd research_portal
