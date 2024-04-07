from django.core.management.base import BaseCommand
from events.models import Theme
from events.enums import EventThemeEnum


class Command(BaseCommand):
    help = 'Добавляет первичный список базовых тематик'

    def handle(self, *args, **options):
        for status in EventThemeEnum:
            if not Theme.objects.filter(name=status.value):
                Theme.objects.create(name=status.value)
