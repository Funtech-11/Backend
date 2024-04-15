import sys

from django.core.management.base import BaseCommand
from users.models import Agreement, Expertise, Stack

from events.enums import EventThemeEnum
from events.models import Theme

AGREEMENTS = (
    ('текст1', True),
    ('текст2', False),
    ('текст3', True)
)

EXPERTISE = (
    'Backend',
    'Frontend',
    'Mobile'
)

STACK = ('Java', 'C++', 'Go', 'Другое',
         'Javascript', 'Typescript',
         'Kotlin', 'Swift')


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

            for stack in STACK:
                if not Stack.objects.filter(name=stack):
                    Stack.objects.create(name=stack)
            
            for item in EXPERTISE:
                if not Expertise.objects.filter(name=item):
                    Expertise.objects.create(name=item)
            sys.stdout.write('Загрузка направлений и стэка завершена\n')

        except Exception as e:
            sys.stdout.write(f'Ошибка при загрузке данных: {e}')
