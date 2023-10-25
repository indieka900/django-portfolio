from django.shortcuts import render

def home(request):
    context = {'nav': 'home'}
    return render(request, 'home.html', context)

def about(request):
    context = {'nav': 'about'}
    return render(request, 'about.html', context)

# Create your views here.
