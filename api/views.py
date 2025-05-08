from rest_framework import generics
from django.db.models import Q

from api.serializers import InventorySerializer
from inventory.models import Inventory


class InventoryListView(generics.ListAPIView):
    serializer_class = InventorySerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        supplier = self.request.query_params.get('supplier', None)
        query = Q()
        if name is not None:
            query.add(Q(name__icontains=name), Q.AND)
        if supplier is not None:
            query.add(Q(supplier__name__icontains=supplier), Q.AND)

        queryset = Inventory.objects.select_related('supplier').filter(
            query
        ).only('id', 'name', 'supplier__name', 'availability')
        return queryset