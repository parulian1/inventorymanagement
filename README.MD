#  Inventory Management System

## Overview
This is a project that allowing user to manage their inventory - supplier.

## Features
1. Create an app called “inventory” that will handle showing item listings and viewing each individual
item.
2. Create a view at “/inventory” to display the list of inventories and their suppliers. Data should be
retrieved from a separate Django Rest Framework (DRF) API endpoint available at “/api/inventory”.
No pagination is needed for either of the views. The API endpoint should have filter support to
search by at least name using a URL query parameter, e.g. “?name=<query>”. On the list view, you
should only display the name, supplier name and availability. Optimise database queries where
necessary.
3. Create a view at “/inventory/<id>” to display a selected item from the list page using only views and
template rendering to show the item. Show all information of the item including description, note,
stock, supplier, etc. Use a static image as a thumbnail placeholder. 
4. Add the inventory model to the Django’s built-in admin panel to enable CRUD management of
inventory (Add, update, remove stock). Create a superuser account to access the admin panel.

### Requirements
<hr>

1. Django 5.0+
2. Django REST Framework
3. Postgresql

### Local Configuration
<hr>

1. clone source code from GitHub

2. go to project directory

   ```shell
   cd inventorymanagement
   ```

3. create your own project env
   ```shell
   python3.10 -m venv env
   ```

4. activate your project env
   ``` shell
   source env/bin/activate
   ```

5. go to your project directory and install requirements.txt

   ```shell
   pip install requirements.txt
   ```
   
6. run docker compose

   ```shell
   docker compose up -d
   ```

7. migrate all models to database.

   ```shell
   python3.10 manage.py migrate
   ```
   
8. then run the apps.
   ```shell
   python3.10 manage.py runserver
   ```

9. optional, to create superuser you may run (email and password already provided please take a look inside of inventory commands)
   ```shell
   python3.10 manage.py create_initial_superuser
   ```

10. optional, to create 100 initial data for both supplier and inventory you may run code below
   ```shell
    python3.10 manage.py set_initial_data
   ```
   
### Run The Test and Coverage
<hr>

1. run test case.
   ```shell
   python3.10 manage.py test
   ```
   
   the output should be like this:
   ```shell
   Found 5 test(s).
   Creating test database for alias 'default'...
   System check identified no issues (0 silenced).
   .....
   ----------------------------------------------------------------------
   Ran 5 tests in 0.236s
   
   OK
   Destroying test database for alias 'default'...
   ```
   
2. run test coverage.
   ```shell
   coverage-3.10 run --source='.' manage.py test api
   coverage report
   ```
   
    the output should be like this:
   ```shell
   Name                                                        Stmts   Miss  Cover
   -------------------------------------------------------------------------------
   api/__init__.py                                                 0      0   100%
   api/serializers.py                                              9      0   100%
   api/tests.py                                                   24      0   100%
   api/urls.py                                                     3      0   100%
   api/views.py                                                   16      1    94%
   inventory/__init__.py                                           0      0   100%
   inventory/admin.py                                              4      0   100%
   inventory/apps.py                                               4      0   100%
   inventory/fakers.py                                            15      0   100%
   inventory/helpers.py                                           12      3    75%
   inventory/management/__init__.py                                0      0   100%
   inventory/management/commands/__init__.py                       0      0   100%
   inventory/management/commands/create_initial_superuser.py       8      8     0%
   inventory/management/commands/set_initial_data.py               9      9     0%
   inventory/migrations/0001_initial.py                            6      0   100%
   inventory/migrations/__init__.py                                0      0   100%
   inventory/models.py                                            14      2    86%
   inventory/tests.py                                             21      0   100%
   inventory/urls.py                                               3      0   100%
   inventory/views.py                                             22      3    86%
   invmanagement/__init__.py                                       0      0   100%
   invmanagement/asgi.py                                           4      4     0%
   invmanagement/settings.py                                      23      0   100%
   invmanagement/urls.py                                           5      0   100%
   invmanagement/wsgi.py                                           4      4     0%
   manage.py                                                      11      2    82%
   -------------------------------------------------------------------------------
   TOTAL                                                         217     36    83%
   ```