from django.urls import path
from. import views

app_name='todoapp'
urlpatterns=[
    path('',views.index, name='index'),
    path('todo/',views.todoappView,name='todo'),
    path('addTodoItem/',views.addTodoItem),
    path('deleteTodoItem/<int:id>/',views.deleteTodoItem),
    path('editTodoItem/',views.editTodoItem),
    path('exit/',views.exit)
]