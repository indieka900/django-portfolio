from django.shortcuts import render

def home(request):
    context = {'nav': 'home'}
    return render(request, 'home.html', context)

def about(request):
    context = {'nav': 'about'}
    return render(request, 'about.html', context)

def services(request):
    context = {'nav': 'services'}
    return render(request, 'services.html', context)

# Create your views here.
