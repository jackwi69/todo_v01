from django.shortcuts import render, get_object_or_404, redirect

from .models import Task
from . forms import TaskForm


def index(request):
    #tasks = Task.objects.all()
    tasks = Task.objects.filter(completed=False)
    context = {
        'tasks':tasks
    }
    return render(request, 'app_todo_v02/index.html', context)

def detail_task(request, pk):
    context = {'task': get_object_or_404(Task, pk=pk)}
    return render(request, 'app_todo_v02/detail_task.html', context)

def create_task(request):
    form = TaskForm(request.POST)
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('app_todo_v02:index')

    context = {'form':form}
    return render(request, 'app_todo_v02/create_task.html', context)

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            #return redirect('app_todo_v02:detail_task', args=(pk, pk))
            return redirect('app_todo_v02:index')
    context = {'form':form}
    return render(request, 'app_todo_v02/create_task.html', context)