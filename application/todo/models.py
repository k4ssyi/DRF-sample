from django.db import models
from django.urls import reverse


class Todo(models.Model):
    """Todoモデル."""

    title = models.CharField(verbose_name='タイトル', max_length=50)
    content = models.TextField(verbose_name='内容')
    created_at = models.DateTimeField(
        verbose_name='created_at', auto_now_add=True)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Todo_detail', kwargs={'pk': self.pk})
