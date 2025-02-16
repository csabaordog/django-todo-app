from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.getTask, name='get_task'),
    path('task-list/', views.getAllTasks, name='get_all_tasks'),

]