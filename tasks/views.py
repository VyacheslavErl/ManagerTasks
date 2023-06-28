from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from tasks.models import TaskModel
from tasks.forms import TaskForm

# Create your views here.

def tasks_list(request):
    """ Вывод задач """
    task_list = TaskModel.objects.all()
    return render(request, 'tasks_list.html', {'tasks': task_list})


def add_task(request):
    """ Добавление задач """
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            print(1)
            form.save()
            return redirect('/tasks')
    form = TaskForm

    return render(request, 'tasks_add.html', {'form': form})


def task_info(request, task_id):
    task = TaskModel.objects.get(id=task_id)
    return render(request, 'task_info.html', {'task': task})


def task_del(request, task_id):
    try:
        TaskModel.objects.get(id=task_id).delete()
    except ObjectDoesNotExist:
        pass
    return redirect("/tasks")
