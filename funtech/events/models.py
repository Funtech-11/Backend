import os
from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models
from users.models import User

from events.enums import (
    EventActivityStatusEnum,
    EventFormatEnum,
    EventStatusEnum,
    EventTypeEnum,
)


def get_upload_event_wallpaper_path(instance, filename):
    return os.path.join('wallpaper', filename)


def get_upload_event_photos_path(instance, filename):
    return os.path.join('gallery', filename)


def get_upload_speaker_avatar_path(instance, filename):
    return os.path.join('speakers', filename)


def get_upload_material_path(instance, filename):
    return os.path.join('materials', filename)


class Location(models.Model):
    """ Адрес проведения """

    location_id = models.AutoField(
        primary_key=True,
        verbose_name='id'
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
        verbose_name='Место',
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
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Theme(models.Model):
    """ Тематика """

    theme_id = models.AutoField(
        primary_key=True,
        verbose_name='id'
    )
    name = models.CharField(
        verbose_name='Наименование',
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'


class Event(models.Model):
    """ Мероприятие """

    event_id = models.AutoField(
        primary_key=True,
        verbose_name='id'
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    date_time_start = models.DateTimeField(
        verbose_name='Дата и время',
        null=True
    )
    date_time_end = models.DateTimeField(
        verbose_name='Дата и время',
        blank=True,
        null=True
    )
    location = models.ForeignKey(
        Location,
        verbose_name='Место проведения',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='events'
    )
    max_participants = models.PositiveSmallIntegerField(
        verbose_name='Максимальное кол-во участников',
        validators=[MinValueValidator(1)],
        null=True
    )

    information = models.CharField(
        verbose_name='Описание',
        max_length=200,
        blank=True
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
    activity_status = models.CharField(
        verbose_name='Состояние',
        max_length=255,
        choices=[
            (activity.name, activity.value)
            for activity in EventActivityStatusEnum
        ]
    )
    wallpaper = models.ImageField(
        verbose_name='Обои',
        upload_to=get_upload_event_wallpaper_path,
        blank=True,
    )
    theme = models.ForeignKey(
        Theme,
        verbose_name='Тематика',
        on_delete=models.SET_NULL,
        null=True,
        related_name='events'
    )
    video = models.URLField(
        verbose_name='Ссылка на видеозапись',
        blank=True
    )

    @property
    def status(self):
        if self.date_time_start.date() < datetime.now().date():
            return EventStatusEnum.FINISHED.name
        elif self.users.count() >= self.max_participants:
            return EventStatusEnum.REGISTRATION_CLOSE.name
        else:
            return EventStatusEnum.REGISTRATION_OPEN.name

    @property
    def curent_participants(self):
        return self.users.count()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Photo(models.Model):
    """ Фото """

    photo_id = models.AutoField(
        primary_key=True,
        verbose_name='id',
    )
    file = models.ImageField(
        verbose_name='Фото',
        upload_to=get_upload_event_photos_path,
        blank=True,
    )
    event = models.ForeignKey(
        Event,
        verbose_name='Мероприятие',
        on_delete=models.CASCADE,
        related_name='photos'
    )

    def __str__(self):
        return self.event.name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Speaker(models.Model):
    """ Спикер """

    speaker_id = models.AutoField(
        primary_key=True,
        verbose_name='id'
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
        blank=True
    )

    def __str__(self):
        return f'{self.name}, {self.job}'

    class Meta:
        verbose_name = 'Спикер'
        verbose_name_plural = 'Спикеры'


class Program(models.Model):
    """ Программа """

    program_id = models.AutoField(
        primary_key=True,
        verbose_name='id'
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
        verbose_name='Cпикер',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='programs'
    )
    information = models.TextField(
        verbose_name='Описание',
        max_length=1000,
        blank=True
    )
    event = models.ForeignKey(
        Event,
        verbose_name='Мероприятие',
        on_delete=models.CASCADE,
        related_name='programs'
    )
    material = models.FileField(
        verbose_name='Файл',
        blank=True,
        upload_to=get_upload_material_path
    )

    def __str__(self):
        return f'{self.speaker}: {self.name}'

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'


class UserEvent(models.Model):
    """ Мероприятие пользователя """

    user_event_id = models.AutoField(
        primary_key=True,
        verbose_name='id'
    )
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='events'
    )
    event = models.ForeignKey(
        Event,
        verbose_name='Мероприятие',
        on_delete=models.CASCADE,
        related_name='users'
    )
    agree = models.BooleanField(
        verbose_name='Согласен'
    )
    qr_code = models.CharField(
        'QR код',
        max_length=50,
        null=True  # add validation
    )

    def __str__(self):
        return f'{self.user}, {self.event}'

    class Meta:
        verbose_name = 'Соглашение'
        verbose_name_plural = 'Соглашения'
