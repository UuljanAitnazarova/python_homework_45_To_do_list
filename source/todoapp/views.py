from django.shortcuts import render, get_object_or_404, redirect

from .models import Task
from .forms import TaskForm

def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks':tasks})

def task_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'task_view.html', context={'task': task})

def task_create_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_create.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                description = form.cleaned_data.get('description'),
                full_description = form.cleaned_data.get('full_description'),
                status = form.cleaned_data.get('status'),
                date_completed = form.cleaned_data.get('date_completed'),
            )
            return redirect('task_view', pk=task.id)  
        return render(request, 'task_create.html', context={'form': form}) 



def task_delete_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect("index")
    

def task_update_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'GET':
        form = TaskForm(initial={ 
            'description': task.description,
            'full_description': task.full_description,
            'status': task.status,
            'date_completed': task.date_completed,
        })

        return render(request, 'task_update.html', context={'form':form, 'task':task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():  
            task.description = form.cleaned_data.get('description')
            task.full_description = form.cleaned_data.get('full_description')
            task.status = form.cleaned_data.get('status')
            task.date_completed = form.cleaned_data.get('date_completed')
            task.save()
            return redirect('task_view', pk=task.id )
        return render(request, 'task_create.html', context={'form': form, 'task': task}) 

    

