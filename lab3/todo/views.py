from datetime import datetime
from django.shortcuts import render
from .forms import TodoForm
from .models import Todo

tasks = [
    {'task': 'asd',
     'creation_date': '10/09/2021',
     'due_on_date': '12/09/2021',
     'owner': 'admin',
     'status': False},
    {'task': 'asdasd',
     'creation_date': '10/09/2021',
     'due_on_date': '12/09/2021',
     'owner': 'admin',
     'status': False},
    {'task': 'asddfg',
     'creation_date': '10/09/2021',
     'due_on_date': '12/09/2021',
     'owner': 'admin',
     'status': True}
]


def show_list(request):
    todos = Todo.objects.filter(status=False)
    context = {
        'todos': todos
    }
    return render(request, 'todo_list.html', context)


def add_list(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TodoForm()
    context = {'form': form}
    return render(request, 'form.html', context)


def show_completed(request):
    completed_todos = Todo.objects.filter(status=True)
    context = {
        'completed_todos': completed_todos
    }
    return render(request, 'completed_todo_list.html', context)
