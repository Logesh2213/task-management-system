from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TaskSerializer(serializers.ModelSerializer):
    assigned_user = UserSerializer(read_only=True)
    assigned_user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='assigned_user', write_only=True
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_user', 'assigned_user_id', 'status', 'priority', 'due_date', 'created_at']
