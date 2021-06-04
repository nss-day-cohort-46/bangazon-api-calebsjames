from django.urls import path
from .views import completed_orders
from .views import incompleted_orders

urlpatterns = [
    path('reports/completedorders', completed_orders),
    path('reports/incompletedorders', incompleted_orders),
]