import requests

from django.shortcuts import render, get_object_or_404
from rest_framework.reverse import reverse

from inventory.helpers import get_full_url
from inventory.models import Inventory


def inventory_list(request):
    api_url = get_full_url('api-inventory', request=request)
    search_query = request.GET.get('name', '')
    supplier_query = request.GET.get('supplier', '')
    query_params = {}
    # Construct the API URL with the search query if it exists
    if search_query:
        query_params['name'] = search_query
    if supplier_query:
        query_params['supplier'] = supplier_query
    if query_params.keys():
        api_url = get_full_url('api-inventory', request=request, query_params=query_params)
    # Fetch data from the API
    response = requests.get(api_url)
    inventories = response.json()  # Assuming the response is in JSON format
    return render(request, 'inventory/list.html', {'inventories': inventories})


def inventory_detail(request, id):
    item = get_object_or_404(Inventory, id=id)
    return render(request, 'inventory/detail.html', {'item': item})
