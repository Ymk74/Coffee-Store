from django.shortcuts import render , get_object_or_404
from datetime import datetime
from .models import Product

# Create your views here.
def products(request):
    pro = Product.objects.all()

    name = None
    description =None
    pfrom = None
    pto = None

    if 'search_name' in request.GET:
        name = request.GET['search_name']
        if name :
            pro = pro.filter(name__icontains=name)

    if 'search_description' in request.GET:
        description = request.GET['search_description']
        if description :
            pro = pro.filter(description__icontains=description)
        
    if 'search_price_from' in request.GET and 'search_price_to' in request.GET :
        pfrom = request.GET['search_price_from']
        pto = request.GET['search_price_to']
        if pfrom and pto :
            if  pfrom.isdigit() and pto.isdigit():
                pro = pro.filter( price__gte=pfrom , price__lte=pto )
                

    items = {
        'products' : pro,
        'name' : name ,
        'description' : description ,
    }
    return render(request , 'products.html' ,items)
    

def product(request,id):
    context = {
        'pro' :get_object_or_404(Product,pk=id)
    }
    return render(request , 'product.html',context)
    

    
def search(request):
    return render(request , 'search.html')
    