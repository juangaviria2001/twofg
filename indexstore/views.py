from django.shortcuts import render
from .models import Groupclothes

# Create your views here.

def bs5(request):
    return render(request, 'indexstore.html')

def catalog(request):
    return render(request, 'catalog.html')

def products(request):
    clothes = Groupclothes.objects.all()
    return render(request, 'products.html', {'clothes': clothes})
