from django.urls import path

from todoapp.views import index_view, task_view, task_create_view, task_delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('task/<int:pk>/', task_view, name='task_view'),
    path('tasks/add/', task_create_view, name='task_create'),
    path('task/delete/<int:pk>/', task_delete_view, name='task_delete'), 
]