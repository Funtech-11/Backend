from django.core.validators import MinValueValidator
from django.db import models

from .enums import (
    EventActivityStatusEnum,
    EventFormatEnum,
    EventStatusEnum,
    EventThemeEnum,
    EventTypeEnum,
)


class Event(models.Model):
    """Модель мероприятия"""

    event_id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Название', max_length=255)
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    city = models.CharField(verbose_name='Город', max_length=255)
    address = models.CharField(verbose_name='Адрес', max_length=255)

    number_of_paricipants = models.PositiveSmallIntegerField(
        verbose_name='Число участников',
        validators=[MinValueValidator(1)]
    )

    information = models.CharField(verbose_name='Описание', max_length=200)

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
        choices=[
            (event_format.name, event_format.value)
            for event_format in EventFormatEnum
        ]
    )

    theme = models.CharField(
        verbose_name='Тематика',
        max_length=255,
        choices=[
            (theme.name, theme.value)
            for theme in EventThemeEnum
        ]
    )

    program_time = models.TimeField(verbose_name='Время')
    program_name = models.CharField(verbose_name='Название', max_length=255)

    program_speaker = models.CharField(
        verbose_name='Докладчик',
        max_length=255
    )

    program_information = models.TextField(
        verbose_name='Описание',
        max_length=1000
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
