from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def loginpanel(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'error' : 'Nombre de usuario o contraseña incorrectos y/o no existen'
            })
        else:
            user.save()
            login(request, user)
            return redirect('panelindex')

@login_required
def panelindex(request):
    return render(request, 'panelindex.html')

def signout(request):
    logout(request)
    return redirect('loginpanel')
    
