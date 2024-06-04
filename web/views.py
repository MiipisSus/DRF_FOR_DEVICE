from django.shortcuts import render, redirect

def home_page(request):
    return redirect('login')


def login_page(request):
    context = {}
    
    return render(request, 'web/login_page.html', context)
