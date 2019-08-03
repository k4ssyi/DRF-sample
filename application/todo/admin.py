from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
