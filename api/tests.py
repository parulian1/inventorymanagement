from rest_framework.test import APITestCase

from inventory.fakers import InventoryFactory


class InventoryAPITests(APITestCase):
    def setUp(self):
        self.inventory = InventoryFactory()
        InventoryFactory(name="Test Inventory")

    def test_list_inventories(self):

        with self.subTest("Test list inventories"):
            response = self.client.get('/api/inventory/')
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertTrue(len(data))
            self.assertEqual(data[0]['name'], self.inventory.name)
            self.assertEqual(data[0]['supplier_name'], self.inventory.supplier.name)

        with self.subTest("Test list inventories filtered by name"):
            response = self.client.get(f'/api/inventory/?name={self.inventory.name}')
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['name'], self.inventory.name)

        with self.subTest("Test list inventories filtered by supplier"):
            response = self.client.get(f'/api/inventory/?supplier={self.inventory.supplier.name}')
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['name'], self.inventory.name)
            self.assertEqual(data[0]['supplier_name'], self.inventory.supplier.name)

        with self.subTest("Test list inventories filtered by name and supplier"):
            response = self.client.get(f'/api/inventory/?name={self.inventory.name}&supplier={self.inventory.supplier.name}')
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['name'], self.inventory.name)
            self.assertEqual(data[0]['supplier_name'], self.inventory.supplier.name)

        with self.subTest("Test list inventories filtered with no result"):
            response = self.client.get('/api/inventory/?name=NonExistent')
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(len(data), 0)