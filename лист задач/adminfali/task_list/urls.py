from django.contrib import admin
from django.urls import path
from task_list.views import *

urlpatterns = [
    path('get_all/', get_all, name='get_all'),
    path('addTask/', add_task, name='add_task'),
    path('deleteTask/', delet_task_by_id, name='delete_Task'),
]
