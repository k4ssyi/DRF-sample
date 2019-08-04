from rest_framework import generics
from django_filters import rest_framework as filters
from ..todo.models import Todo
from .serializers import TodoSerializer


class TodoFilter(filters.FilterSet):
    """"複数の検索条件に対応させる"""
    title = filters.CharFilter(field_name="title", lookup_expr="contains")

    class Meta:
        model = Todo
        fields = ['title', 'content']


class TodoListCreateAPIView(generics.ListCreateAPIView):
    """Todoリスト一覧表示、登録API."""

    serializer_class = TodoSerializer
    queryset = Todo.objects.prefetch_related('author')
    filter_class = TodoFilter
