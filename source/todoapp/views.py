from django.shortcuts import render

from .models import Task


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks':tasks})

def task_view(request):
    task_id = request.GET.get('id')
    task = Task.objects.get(id=task_id)
    return render(request, 'task_view.html', context={'task': task})

def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'status_choice': Task.STATUS_CHOICES})
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        date_completed = request.POST.get('date_completed')
        if not date_completed:
            date_completed=None

        task = Task.objects.create(
            description=description,
            status=status,
            date_completed= date_completed
        )
        return render(request, 'task_view.html', context = {'task': task})