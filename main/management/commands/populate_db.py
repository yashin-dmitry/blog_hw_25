import json
from django.core.management.base import BaseCommand
from main.models import Category, Product


class Command(BaseCommand):
    @staticmethod
    def json_read_categories():
        with open('fixtures/main_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [item for item in data if item['model'] == 'main.category']

    @staticmethod
    def json_read_products():
        with open('fixtures/main_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [item for item in data if item['model'] == 'main.product']

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_for_create = []
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['fields']['name'],
                         description=category['fields']['description'])
            )
        Category.objects.bulk_create(category_for_create)

        product_for_create = []
        for product in Command.json_read_products():
            category = Category.objects.get(pk=product['fields']['category'])
            product_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        preview_image=product['fields']['preview_image'],
                        category=category,
                        purchase_price=product['fields']['purchase_price'],
                        manufactured_at=product['fields']['manufactured_at'])
            )
        Product.objects.bulk_create(product_for_create)
