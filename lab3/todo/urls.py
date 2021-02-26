from django.urls import path
from todo.views import *

urlpatterns = [
    path('', show_list),
    path('add_todo/', add_list),
    path('completed_todo_list/', show_completed),
]
