from django.shortcuts import render , get_object_or_404
from datetime import datetime
from .models import Product

# Create your views here.
def products(request):
    pro = Product.objects.all()

    name = None
    if 'search_name' in request.GET:
        name = request.GET['search_name']
    if name :
        pro = pro.filter(name__icontains=name)
    items = {
        'products' : pro,
        'name' : name
    }
    return render(request , 'products.html' ,items)
    

def product(request,id):
    context = {
        'pro' :get_object_or_404(Product,pk=id)
    }
    return render(request , 'product.html',context)
    

    
def search(request):
    return render(request , 'search.html')
    