from rest_framework import serializers
from todo.models import *


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'due_on_date', 'status')


class ListSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = ('id', 'name', 'todos')
