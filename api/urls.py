from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.getTask, name='get_task'),

]