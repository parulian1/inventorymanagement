from rest_framework.test import APITestCase

from inventory.fakers import InventoryFactory


class InventoryAPITests(APITestCase):
    def setUp(self):
        self.inventory = InventoryFactory()
        InventoryFactory(name="Test Inventory")

    def test_list_inventories(self):
        response = self.client.get('/api/inventory/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(len(data))
        self.assertEqual(data[0]['name'], self.inventory.name)
        self.assertEqual(data[0]['supplier_name'], self.inventory.supplier.name)

    def test_filter_inventories_by_name(self):
        response = self.client.get(f'/api/inventory/?name={self.inventory.name}')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], self.inventory.name)

    def test_filter_inventories_no_result(self):
        response = self.client.get('/api/inventory/?name=NonExistent')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 0)