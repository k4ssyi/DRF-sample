from rest_framework import generics

from ..todo.models import Todo
from .serializers import TodoSerializer


class TodoListCreateAPIView(generics.ListCreateAPIView):
    """Todoリスト一覧表示、登録API."""

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
