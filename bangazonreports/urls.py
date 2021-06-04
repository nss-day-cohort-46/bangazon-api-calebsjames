from django.urls import path
from .views import completed_orders
from .views import incompleted_orders
from .views import expensive_products
from .views import inexpensive_products

urlpatterns = [
    path('reports/completedorders', completed_orders),
    path('reports/incompletedorders', incompleted_orders),
    path('reports/expensiveproducts', expensive_products),
    path('reports/inexpensiveproducts', inexpensive_products),
]