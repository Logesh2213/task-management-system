from rest_framework import viewsets, filters
from .models import Task, UserProfile
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render
from django.views.generic import ListView

# Frontend Task List View
class TaskListView(ListView):
    model = Task
    template_name = 'projects/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 20

# REST API ViewSets
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save()
