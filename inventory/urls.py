from django.urls import path

from inventory.views import inventory_list, inventory_detail

urlpatterns = [
    path('', inventory_list, name='inventory_list'),
    path('<int:id>/', inventory_detail, name='inventory_detail'),
]
