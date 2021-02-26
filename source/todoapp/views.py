from django.shortcuts import render, get_object_or_404, redirect

from .models import Task


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks':tasks})

def task_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'task_view.html', context={'task': task})

def task_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'status_choice': Task.STATUS_CHOICES})
    elif request.method == 'POST':
        description = request.POST.get('description')
        full_description = request.POST.get('full_description')
        status = request.POST.get('status')
        date_completed = request.POST.get('date_completed')
        if not date_completed:
            date_completed=None

        task = Task.objects.create(
            description=description,
            full_description = full_description,
            status=status,
            date_completed= date_completed
        )
        return redirect('task_view', pk=task.pk)


def task_delete_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect("index")
    
    return render(request, 'task_delete.html', context={'task': task})

