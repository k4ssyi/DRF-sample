from django.urls import path

from ..apiv1 import views

app_name = 'apiv1'
urlpatterns = [
    # 一覧表示
    path('todos/', views.TodoListCreateAPIView.as_view())
]
