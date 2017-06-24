from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo


def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos':todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
       'todo':todo
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/todos')
    else:
        return render(request, 'add.html')

"""
def edit(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/todos')
    else:
        return render(request, 'edit.html')


def delete(request):
    title = Todo.objects.get(id=id).update(title=request.POST.get('title'))
    text = Todo.objects.get(id=id).update(text=request.POST.get('text'))
    todo = Todo(title=title, text=text)
    todo.delete(save=True)
    return redirect('/todos')
"""
