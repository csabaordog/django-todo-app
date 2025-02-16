from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.getTask, name='get_task'),
    path('task-list/', views.getAllTasks, name='get_all_tasks'),
    path('task-create/', views.createTask, name='create_task'),
    path('task-update/<int:pk>/', views.updateTask, name='update_task'),
    path('task-delete/<int:pk>/', views.deleteTask, name='delete_task'),
]