from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('todo_update/<int:slno>',views.todo_update,name='todo_update'),
    path('todo_delete/<int:slno>',views.todo_delete,name='todo_delete'),
]