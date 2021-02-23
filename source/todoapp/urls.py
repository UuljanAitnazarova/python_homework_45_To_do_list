from django.urls import path

from todoapp.views import index_view

urlpatterns = [
    path('', index_view)
]