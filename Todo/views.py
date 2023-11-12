from django.shortcuts import render, redirect

from .models import Todo

from django.contrib.auth.decorators import login_required


# /todo/ # GET REQ
@login_required(login_url="auth:login_user")
def get_todo_lists(request):
    todos = Todo.objects.filter(host=request.user)
    context = {
        "username": request.user,
        "list": todos,
    }
    return render(request, "Todo/todos.html", context)


# /todo/add/ # POST REQ
@login_required(login_url="auth:login_user")
def add_todo(request):
    if request.POST.get('content') is not None:
        todo = Todo.objects.create(
            host=request.user,
            content=request.POST.get('content')
        )
        todo.save()
        return redirect('todo:get_todo_lists')



# /todo/delete/<int>/ # POST REQ
@login_required(login_url="auth:login_user")
def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == 'POST':
        todo.delete()
        return redirect("todo:get_todo_lists")
    
    context={"todo": todo.content}
    return render(request, 'Todo/delete.html', context)

# /todo/change/<int>/ # POST REQ
@login_required(login_url="auth:login_user")
def change_todo_tatus(request, pk):
    if request.method == 'POST':
        todo = Todo.objects.get(id=pk)
        todo.is_compleated = not todo.is_compleated
        todo.save()
        return redirect("todo:get_todo_lists")
