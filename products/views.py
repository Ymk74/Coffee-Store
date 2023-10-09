from django.shortcuts import render
from datetime import datetime
from .models import Product

# Create your views here.
def products(request):
    items = {
        'products' : Product.objects.all()
    }
    return render(request , 'products.html' ,items)
    

def product(request):
    return render(request , 'product.html')
    

    
def search(request):
    return render(request , 'search.html')
    