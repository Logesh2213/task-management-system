from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskListView, TaskViewSet, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('api/', include(router.urls)),
]
