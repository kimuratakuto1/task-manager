from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()  # すべてのタスクを取得
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # タスクを保存
            return redirect('task_list')  # 保存後、タスク一覧にリダイレクト
        else:
            print(form.errors)  # フォームのエラーを表示
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})
