from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url='login')
def home_page(request):
    return render(request, 'web/home_page.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. \nPlease try again.")
    
    return render(request, 'web/login_page.html')

def logout_page(request):
    logout(request)
    return redirect('home')

