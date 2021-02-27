from django.urls import path
from todo.views import *

urlpatterns = [
    path('', show_list),
    path('<int:id>', show_todo),
    path('add_todo/', add_list),
    path('completed_todo_list/', show_completed),
]
