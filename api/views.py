from rest_framework import generics
from django.db.models import Q

from api.serializers import InventorySerializer
from inventory.models import Inventory


class InventoryListView(generics.ListAPIView):
    serializer_class = InventorySerializer

    def get_queryset(self):
        queryset = Inventory.objects.select_related('supplier')
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(
                Q(name__icontains=name)
            )
        return queryset