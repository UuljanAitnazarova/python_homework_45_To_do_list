from django.shortcuts import render

from .models import Task


def index_view(request):
    tasks = Task.objects.all()
    
    return render(request, 'index.html', context={'tasks':tasks})