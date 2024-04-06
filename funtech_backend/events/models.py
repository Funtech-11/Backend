import os

from django.core.validators import MinValueValidator
from django.db import models

from events.enums import (
    EventActivityStatusEnum,
    EventFormatEnum,
    EventStatusEnum,
    EventTypeEnum,
)


def get_upload_wallpaper(instance, filename):
    """Создание директории для хранения файлов отдельного мероприятия"""
    event_folder = instance.name
    return os.path.join(event_folder, 'gallery', filename)


def get_upload_path(instance, filename):
    pass


class Event(models.Model):
    """Мероприятие"""

    event_id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    date_time = models.DateTimeField(
        verbose_name='Дата и время',
        null=True
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET('location.building'),
        null=True
    )
    number_of_participants = models.PositiveSmallIntegerField(
        verbose_name='Число участников',
        validators=[MinValueValidator(1)],
    )
    information = models.CharField(
        verbose_name='Описание',
        max_length=200, blank=True
    )
    event_type = models.CharField(
        verbose_name='Тип',
        max_length=255,
        choices=[
            (event_type.name, event_type.value)
            for event_type in EventTypeEnum
        ]
    )
    event_format = models.CharField(
        verbose_name='Формат',
        max_length=255,
        blank=True,
        choices=[
            (event_format.name, event_format.value)
            for event_format in EventFormatEnum
        ]
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=255,
        choices=[
            (status.name, status.value)
            for status in EventStatusEnum
        ]
    )
    activity_status = models.CharField(
        verbose_name='Состояние',
        max_length=255,
        choices=[
            (activity.name, activity.value)
            for activity in EventActivityStatusEnum
        ]
    )
    wallpaper = models.ImageField(
        verbose_name='Фото',
        upload_to=get_upload_wallpaper,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Location(models.Model):
    "Адрес проведения"

    location_id = models.AutoField(
        primary_key=True
    )
    city = models.CharField(
        verbose_name='Город',
        max_length=255
    )

    address = models.CharField(
        verbose_name='Адрес',
        max_length=255,
        blank=True
    )
    builing = models.CharField(
        verbose_name='Строение',
        max_length=255
    )
    metro_station = models.CharField(
        verbose_name='Станция метро',
        max_length=255,
        blank=True
    )

    def __str__(self):
        return f'{self.city}, {self.builing}'

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Program(models.Model):
    """Программа мероприятия"""

    program_id = models.AutoField(primary_key=True)

    name = models.CharField(verbose_name='Название', max_length=255)
    time = models.TimeField(verbose_name='Время')
    speaker = models.CharField(verbose_name='Докладчик', max_length=255)
    information = models.TextField(verbose_name='Описание', max_length=1000)

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='programs'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'


class Theme(models.Model):
    """Тематика"""

    theme_id = models.AutoField(primary_key=True)

    name = models.CharField(
        verbose_name='Название', max_length=255, unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'


class EventTheme(models.Model):
    """Тематика мероприятия"""

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='themes'
    )

    def __str__(self):
        return f'Тематика {self.theme} мероприятия {self.event}'

    class Meta:
        verbose_name = 'Тематика мероприятия'
        verbose_name_plural = 'Тематики мероприятий'


class Matetial(models.Model):
    """Материал мероприятия"""

    material_id = models.AutoField(primary_key=True)

    file = models.FileField(verbose_name='Файл', upload_to=get_upload_path)

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='materials'
    )

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Video(models.Model):
    """Видеозапись мероприятия"""

    video_id = models.AutoField(primary_key=True)

    url = models.URLField(verbose_name='Сcылка')

    event = models.OneToOneField(
        Event, on_delete=models.CASCADE, related_name='video'
    )

    class Meta:
        verbose_name = 'Видеозапись'
        verbose_name_plural = 'Видеозаписи'
