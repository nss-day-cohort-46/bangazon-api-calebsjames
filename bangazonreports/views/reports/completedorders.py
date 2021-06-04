from bangazonapi.models import Order
from django.shortcuts import render
from django.db.models import Sum

def completed_orders(request):
    
    orders = Order.objects.filter(payment_type__isnull = False).annotate(total=Sum("lineitems__product__price"))
    
    template = 'orders/completedorders.html'
    
    context = {'orders' : orders}
    
    return render(request, template, context)