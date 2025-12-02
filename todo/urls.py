from django.urls import path
from todo import views

urlpatterns = [
    path('todo/', views.TodoListView.as_view(), name='todo-list'),
    path('todo/<int:pk>/', views.TodoDetailView.as_view(), name='todo-detail'),
]
