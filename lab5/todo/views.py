from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import *
from .serializers import *


class ListViewSet(viewsets.ViewSet):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ListSerializer

    def get_queryset(self):
        return Todo.objects.filter(status=False)

    def list(self, request):
        serializer = ListSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class TodoViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self, id):
        return Todo.objects.filter(list_id=id, status=False)

    def todo_by_list(self, request, id):
        serializer = ListSerializer(self.get_queryset(id), many=True)
        return Response(serializer.data)


class CompletedTodoViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self, id):
        return Todo.objects.filter(list_id=id, status=True)

    def completed_todo_by_list(self, request, id):
        serializer = ListSerializer(self.get_queryset(id), many=True)
        return Response(serializer.data)



# def show_all(request):
#     todos = Todo.objects.filter(status=False)
#     context = {
#         'todos': todos,
#         'list': {'name': 'All lists'}
#     }
#     return render(request, 'todo_list.html', context)
#
#
# def show_list(request, id):
#     todos = Todo.objects.filter(list_id=id, status=False)
#     list_name = List.objects.get(id=id)
#     context = {
#         'todos': todos,
#         'list': list_name
#     }
#     return render(request, 'todo_list.html', context)
#
#
# def show_completed(request, id):
#     completed_todos = Todo.objects.filter(list_id=id, status=True)
#     list_name = List.objects.get(id=id)
#     context = {
#         'completed_todos': completed_todos,
#         'list': list_name
#     }
#     return render(request, 'completed_todo_list.html', context)
