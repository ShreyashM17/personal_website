from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.
def index(request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        new_Todo = Todo(
            title=request.POST['title']
        )
        new_Todo.save()
        return redirect('/todo_list')
    return render(request, 'todo_list.html', {'todo': todo})


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/todo_list')

