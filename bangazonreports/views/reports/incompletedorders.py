from bangazonapi.models import Order
from django.shortcuts import render
from django.db.models import Sum

def incompleted_orders(request):
    
    orders = Order.objects.filter(payment_type__isnull = True).annotate(total=Sum("lineitems__product__price"))
    
    template = 'orders/incompletedorders.html'
    
    context = {'orders' : orders}
    
    return render(request, template, context)