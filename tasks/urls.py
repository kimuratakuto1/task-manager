from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # タスク一覧のURL
    path('add/', views.add_task, name='add_task'),  # タスク追加のURL
]
