from rest_framework import serializers

from inventory.models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    supplier_name = serializers.SerializerMethodField()

    def get_supplier_name(self, obj):
        return obj.supplier.name

    class Meta:
        model = Inventory
        fields = (
            'id',
            'name',
            'supplier_name',
            'availability',
        )
