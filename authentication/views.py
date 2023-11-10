from django.shortcuts import render


def login_user(request):
    return render(request, 'authentication/login.html')

def logout_user(request):
    return render(request, 'authentication/logout.html')

def register_user(request):
    return render(request, 'authentication/register.html')