from django.shortcuts import render

# Create your views here.

def bs5(request):
    return render(request, 'indexstore.html')

def catalog(request):
    return render(request, 'catalog.html')

def products(request):
    return render(request, 'products.html')
