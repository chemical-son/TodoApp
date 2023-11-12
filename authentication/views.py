from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# /auth/login/ # POST REQ
def login_user(request):
    if request.user.is_authenticated:
        return redirect("todo:get_todo_lists")

    elif request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exits")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("todo:get_todo_lists")
        else:
            messages.error(request, "Usernaem or password does not correct")

    return render(request, "authentication/login.html")


# /auth/register/ # POST REQ
def register_user(request):

    if request.method == "POST":
        username = request.POST.get("username").lower()
        email = request.POST.get("email").lower()
        password_1 = request.POST.get("password_1")
        password_2 = request.POST.get("password_2")
        
        if password_1 != password_2:
            messages.error(request, "Confirm password dosn't match")
        else:
            try:
                user = User.objects.create_user(username, email, password_1)
                user.save()
                login(request, user)
                return redirect('todo:get_todo_lists')
            except:
                messages.error(request, "this username is arredy taken")        
        

    return render(request, "authentication/register.html")

# /auth/logout/ # POST REQ
@login_required(login_url="auth:login_user")
def logout_user(request):
    logout(request)
    return redirect("auth:login_user")
