# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Author, Todo


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at')
    list_filter = ('created_at',)
    raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
