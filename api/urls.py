from django.urls import path

from api.views import InventoryListView

urlpatterns = [
    path('inventory/', InventoryListView.as_view(), name='api-inventory'),
]