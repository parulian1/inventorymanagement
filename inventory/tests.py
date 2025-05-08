from django.test import TestCase, Client
from django.urls.base import reverse
from unittest.mock import patch

from inventory.fakers import InventoryFactory
from inventory.models import Inventory


class InventoryViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        for _ in range(10):
            InventoryFactory()
        self.first_inventory = Inventory.objects.first()

    @patch('requests.get')
    def test_inventory_list_view(self, mock_get):
        mock_get.return_value.json.return_value = [
            {
                'id': self.first_inventory.id,
                'name': self.first_inventory.name,
                'supplier_name': self.first_inventory.supplier.name,
                'availability': self.first_inventory.availability,
            }
        ]
        response = self.client.get(reverse('inventory_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.first_inventory.name)

    def test_inventory_detail_view(self):
        response = self.client.get(reverse('inventory_detail', args=(self.first_inventory.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.first_inventory.name)
