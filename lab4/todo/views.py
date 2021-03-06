from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo, List


def show_all(request):
    todos = Todo.objects.filter(status=False)
    context = {
        'todos': todos,
        'list': {'name': 'All lists'}
    }
    return render(request, 'todo_list.html', context)


def show_list(request, id):
    todos = Todo.objects.filter(list_id=id, status=False)
    list_name = List.objects.get(id=id)
    context = {
        'todos': todos,
        'list': list_name
    }
    return render(request, 'todo_list.html', context)


def show_completed(request, id):
    completed_todos = Todo.objects.filter(list_id=id, status=True)
    list_name = List.objects.get(id=id)
    context = {
        'completed_todos': completed_todos,
        'list': list_name
    }
    return render(request, 'completed_todo_list.html', context)
