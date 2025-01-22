from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Groupclothes

# Create your views here.

def bs5(request):
    return render(request, 'indexstore.html')

def catalog(request):
    return render(request, 'catalog.html')

def products(request):
    #clothes = Groupclothes.objects.all()
    clotheType = request.GET.get('clotheType')
    clothes = Groupclothes.objects.filter(type=clotheType)
    return render(request, 'products.html', {'clothes': clothes,'clotheType': clotheType})
    

