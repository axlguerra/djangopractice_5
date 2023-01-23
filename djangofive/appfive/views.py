from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'appfive/index.html')

def register(request):
    return render(request, 'appfive/registration.html')

def base(request):
    return render(request, 'appfive/base.html')