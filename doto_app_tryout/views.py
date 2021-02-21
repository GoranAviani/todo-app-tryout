from django.shortcuts import render, redirect

def index(request):
    return redirect('dashboard') if request.user.is_authenticated else render(request, 'index.html')
