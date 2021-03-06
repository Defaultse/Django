from django.urls import path
from todo.views import *

urlpatterns = [
    path('', show_all),
    path('<int:id>', show_list),
    path('<int:id>/completed_todo_list/', show_completed),
]