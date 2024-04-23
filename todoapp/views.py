from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .models import TodoListItem

# Create your views here.

def index(request):
    return render(request,'index.html')

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()

    return render(request,'todolist.html',{'all_items':all_todo_items})


def addTodoItem(request):
    new_item=TodoListItem()
    new_item.content=request.POST.get('content')
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodoItem(request,id):
    d = TodoListItem.objects.get(id=id)
    d.delete()
    return HttpResponseRedirect('/todo/')

def editTodoItem(request,id):
    edit_item = TodoListItem.objects.get(id=id)
    edit_item.content = request.POST.get('content')
    edit_item.save()
    return HttpResponseRedirect('/todo/')

def exit(request):
    return render(request,'index.html')
