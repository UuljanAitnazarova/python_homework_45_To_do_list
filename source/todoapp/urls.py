from django.urls import path

from todoapp.views import index_view, task_view, task_create_view

urlpatterns = [
    path('', index_view),
    path('task/', task_view),
    path('tasks/add/', task_create_view),
]