import os
from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models

from events.enums import (
    EventActivityStatusEnum,
    EventFormatEnum,
    EventStatusEnum,
    EventTypeEnum,
)


def get_upload_wallpaper_path(instance, filename):
    event_folder = f'{instance.name}, {instance.location.city}'
    return os.path.join(event_folder, 'wallpaper', filename)


def get_upload_event_photos_path(instance, filename):
    event_folder = f'{instance.name}, {instance.location.city}'
    return os.path.join(event_folder, 'gallery', filename)


def get_upload_speaker_avatar_path(instance, filename):
    return os.path.join('speakers', filename)


def get_upload_material_path(instance, filename):
    event_folder = f'{instance.event.name}, {instance.event.location.city}'
    program_folder = instance.name
    return os.path.join(event_folder, program_folder, 'materials', filename)


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


class Theme(models.Model):
    """Тематика"""

    theme_id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'


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
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='events'
    )
    max_participants = models.PositiveSmallIntegerField(
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
            (event_type.value, event_type.name)
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
        upload_to=get_upload_wallpaper_path,
        blank=True,
    )
    theme = models.ForeignKey(
        Theme,
        on_delete=models.SET_NULL,
        null=True,
        related_name='events'
    )
    video = models.URLField(
        verbose_name='Ссылка на видеозапись'
    )

    @property
    def status(self):
        if self.date_time.date() < datetime.now().date():
            return EventStatusEnum.FINISHED.name
        else:
            return EventStatusEnum.REGISTRATION_OPEN.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Photo(models.Model):
    """Фото в галерею"""

    photo_id = models.AutoField(
        primary_key=True
    )
    file = models.ImageField(
        verbose_name='Фото',
        upload_to=get_upload_wallpaper_path,
        blank=True,
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='photos'
    )


class Speaker(models.Model):
    """Спикер мероприятия"""

    speaker_id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        verbose_name='Имя',
        max_length=255
    )
    job = models.CharField(
        verbose_name='Позиция',
        max_length=255
    )
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to=get_upload_speaker_avatar_path,
        null=True
    )

    def __str__(self):
        return f'{self.name} - {self.job}'

    class Meta:
        verbose_name = 'Докладчик'
        verbose_name_plural = 'Докладчики'


class Program(models.Model):
    """Программа мероприятия"""

    program_id = models.AutoField(
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
    speaker = models.ForeignKey(
        Speaker,
        on_delete=models.SET_NULL,
        null=True,
        related_name='programs'
    )
    information = models.TextField(
        verbose_name='Описание',
        max_length=1000
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='programs'
    )
    material = models.FileField(
        verbose_name='Файл',
        upload_to=get_upload_material_path
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'
