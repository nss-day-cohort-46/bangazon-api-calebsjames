from bangazonapi.models import Product
from django.shortcuts import render


def inexpensive_products(request):
    
    products = Product.objects.filter(price__lt = 1000)
    
    template = 'products/inexpensiveproducts.html'
    
    context = {'products' : products}
    
    return render(request, template, context)