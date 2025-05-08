import factory

from inventory.models import Supplier, Inventory


class SupplierFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')

    class Meta:
        model = Supplier



class InventoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    description = factory.Faker('text')
    note = factory.Faker('text')
    stock = factory.Faker('random_int', min=0, max=100)
    availability = factory.Faker('boolean')
    supplier = factory.SubFactory(SupplierFactory)

    class Meta:
        model = Inventory