from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'Create initial superuser'

    def handle(self, *args, **kwargs):
        print('Setting initial superuser...')
        get_user_model().objects.create_superuser(email='kiratechdev@kiratech.com.au', password='kiratech1986')
        print('Initial superuser created successfully!')
