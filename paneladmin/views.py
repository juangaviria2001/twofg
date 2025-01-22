from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def panelindex(request):
    return render(request, 'panelindex.html')

