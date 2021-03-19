from django.urls import path
from rest_framework import routers

from todo.views import *

urlpatterns = {
    path('', ListViewSet.as_view({'get': 'list'})),
    path('<int:id>/', TodoViewSet.as_view({'get': 'todo_by_list'})),
    path('<int:id>/completed/', CompletedTodoViewSet.as_view({'get': 'completed_todo_by_list'})),
}
