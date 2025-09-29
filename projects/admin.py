from django.contrib import admin
from .models import UserProfile, Task

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'registration_date')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_user', 'status', 'priority', 'due_date', 'created_at')
    list_filter = ('status', 'priority', 'due_date')
    search_fields = ('title', 'description', 'assigned_user__username')
