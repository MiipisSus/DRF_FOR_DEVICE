from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from device_info.models import *
from device_info.forms import *

@login_required(login_url='login')
def home_page(request):
    context = {
        'header_name': 'Home'
    }
    return render(request, 'web/home_page.html', context)

def basic_page(request):
    instance = DeviceBasicInfo.objects.first()
    if request.method == 'POST':
        form = DeviceBasicForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('basic')
    else:
        form = DeviceBasicForm(instance=instance)
        
    context = {
        'header_name': 'System / Basic Information',
        'sub_page': 'basic_page',
        'instance': instance,
        'form': form
    }
    return render(request, 'web/home_page.html', context)
    
    
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

