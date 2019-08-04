import uuid
from django.db import models
from django.urls import reverse


class Author(models.Model):
    """著者モデル."""

    class Meta:
        db_table = "author"
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="著者名", max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})


class Todo(models.Model):
    """Todoモデル."""

    author = models.ManyToManyField(Author, verbose_name="著者", null=True)
    title = models.CharField(verbose_name='タイトル', max_length=50)
    content = models.TextField(verbose_name='内容')
    created_at = models.DateTimeField(
        verbose_name='created_at', auto_now_add=True)

    class Meta:
        db_table = "todo"
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Todo_detail', kwargs={'pk': self.pk})
