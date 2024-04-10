import sys

from django.core.management.base import BaseCommand
from events.models import Theme
from events.enums import EventThemeEnum
from users.models import Agreement, Expertise, Stack

AGREEMENTS = (
    ('текст1', True),
    ('текст2', False),
    ('текст3', True)
)

STACK = {
    'Backend': ('Java', 'C++', 'Go', 'Другое'),
    'Frontend': ('Javascript', 'Typescript', 'Другое'),
    'Mobile': ('Kotlin', 'Swift', 'Другое')
}


class Command(BaseCommand):
    help = 'Добавляет первичный список базовых тематик, \
            соглашений, направлений и стэка'

    def handle(self, *args, **options):
        try:
            for status in EventThemeEnum:
                if not Theme.objects.filter(name=status.name):
                    Theme.objects.create(name=status.name)
            sys.stdout.write('Загрузка тематик завершена\n')

            for agreement in AGREEMENTS:
                if not Agreement.objects.filter(text=agreement[0]):
                    Agreement.objects.create(text=agreement[0],
                                             is_required=agreement[1])
            sys.stdout.write('Загрузка соглашений завершена\n')

            for expertise, stack in STACK.items():
                if not Expertise.objects.filter(name=expertise):
                    object = Expertise.objects.create(name=expertise)
                    for stack_item in stack:
                        Stack.objects.create(name=stack_item,
                                             expertise=object)
            sys.stdout.write('Загрузка направлений и стэка завершена\n')
        except Exception as e:
            sys.stdout.write(f'Ошибка при загрузке данных: {e}')
