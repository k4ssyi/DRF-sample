from rest_framework import serializers

from ..todo.models import Todo, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)

    class Meta:
        model = Todo
        fields = '__all__'
