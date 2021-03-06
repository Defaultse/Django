from django.contrib import admin
from todo.models import *


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'creation_date', 'due_on_date', 'status', 'list_id']
    ordering = ['due_on_date']
    search_fields = ['id', 'name']
    list_filter = ['due_on_date']


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['name']
