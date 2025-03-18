from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)  # タスクのタイトル
    description = models.TextField(blank=True, null=True)  # タスクの詳細
    due_date = models.DateField(null=True, blank=True)  # 締切日
    completed = models.BooleanField(default=False)  # 完了フラグ

    def __str__(self):
        return self.title
