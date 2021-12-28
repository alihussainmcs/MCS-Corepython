from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import *
# from django.views.generic import ListView, View
from .models import Todo
from django.http import HttpResponseRedirect
# return render(request, 'todos/index.html', context)
# return render(request, template_name)
# first we need route
# views
# testApp
#
# return render(request, 'inex.html', context)
class IndexView(ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos."""
        # .query.get() orm jango inbuil orm whatever query you nee to on atabae
        # Todo.objects.all()
        return Todo.objects.order_by('-created_at')

def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title)

    return redirect('todos:index')

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')