import csv
from django.core.management.base import BaseCommand
from search_app.models import Dish

class Command(BaseCommand):
    help = 'Load dishes from CSV file into the database'

    def handle(self, *args, **kwargs):
        with open('restaurants_small.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Dish.objects.create(
                    name=row['items'], 
                    description=row.get('full_details', ''),
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
