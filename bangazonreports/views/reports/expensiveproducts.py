from bangazonapi.models import Product
from django.shortcuts import render


def expensive_products(request):
    
    products = Product.objects.filter(price__gte = 1000)
    
    template = 'products/expensiveproducts.html'
    
    context = {'products' : products}
    
    return render(request, template, context)