from django.core.management.base import BaseCommand

from inventorymanagement.inventory.fakers import InventoryFactory


class Command(BaseCommand):
    help = 'Set 100 initial data into the database using factory fakers'

    def handle(self, *args, **kwargs):
        print('Setting initial data...')
        for _ in range(100):
            InventoryFactory()
        print('Initial data set successfully! (100 record for both inventory and supplier)')
