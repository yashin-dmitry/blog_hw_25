from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from main.models import Product

class Command(BaseCommand):
    help = 'Create groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Создание группы "Модератор продуктов"
        moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Получение прав
        content_type = ContentType.objects.get_for_model(Product)
        can_unpublish_product = Permission.objects.get(
            codename='can_unpublish_product',
            content_type=content_type,
        )
        delete_product = Permission.objects.get(
            codename='delete_product',
            content_type=content_type,
        )

        # Назначение прав группе
        moderator_group.permissions.add(can_unpublish_product, delete_product)

        self.stdout.write(self.style.SUCCESS('Groups and permissions created successfully'))
