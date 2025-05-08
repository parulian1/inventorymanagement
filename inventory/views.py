import requests

from django.shortcuts import render, get_object_or_404

from inventory.models import Inventory


def inventory_list(request):
    search_query = request.GET.get('name', '')
    # Construct the API URL with the search query if it exists
    api_url = 'http://localhost:8000/api/inventory/'
    if search_query:
        api_url += f'?name={search_query}'
    # Fetch data from the API
    response = requests.get(api_url)
    inventories = response.json()  # Assuming the response is in JSON format
    return render(request, 'inventory/list.html', {'inventories': inventories})


def inventory_detail(request, id):
    item = get_object_or_404(Inventory, id=id)
    return render(request, 'inventory/detail.html', {'item': item})
