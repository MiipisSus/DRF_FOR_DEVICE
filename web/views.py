from django.shortcuts import render, redirect

def main_page(request):
    context = {}
    
    return render(request, 'web/login_page.html', context)
