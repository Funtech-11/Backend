from django.contrib.auth.models import AbstractUser
from django.db import models

from events.enums import EventTypeEnum, ExperienceEnum

MAX_NAME_PASSWORD_CHARS = 30
MAX_WORKPLACE_CHARS = 100
MAX_LINK_CHARS = 100
TRUNCATED_NAME = 10
MAX_EVENT_FORMAT_CHARS = 255
MAX_EXPERIENCE_CHARS = 20


class User(AbstractUser):

    REQUIRED_FIELDS = ('first_name',
                       'last_name')

    password = None  # сбрасываем?
    first_name = models.CharField('Имя',
                                  max_length=MAX_NAME_PASSWORD_CHARS)
    last_name = models.CharField('Фамилия',
                                 max_length=MAX_NAME_PASSWORD_CHARS)
    mobile_number = models.PositiveSmallIntegerField()  # валидация формата?
    employment = models.CharField('Место работы',
                                  max_length=MAX_WORKPLACE_CHARS)
    position = models.CharField('Должность',
                                max_length=MAX_WORKPLACE_CHARS)
    experience = models.CharField(
        verbose_name='Опыт работы',
        max_length=MAX_EXPERIENCE_CHARS,
        choices=[
            exp_type.value for exp_type in ExperienceEnum
        ],
        null=True
    )
    preferred_format = models.CharField(
        verbose_name='Предпочитаемый формат',
        max_length=MAX_EVENT_FORMAT_CHARS,
        choices=[
            event_type.value for event_type in EventTypeEnum
        ]
    )

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Agreement(models.Model):
    """ Соглашение пользователя. """

    text = models.TextField('Текст соглашения')
    link = models.CharField('Ссылка',
                            max_length=MAX_LINK_CHARS,
                            unique=True)

    class Meta:
        verbose_name = 'соглашение'
        verbose_name_plural = 'соглашения'

    def __str__(self):
        return self.id


class UserAgreement(models.Model):
    """ Связь соглашение-пользователь. """

    user = models.OneToOneField(
        User,
        'пользователь'
    )
    agreement = models.OneToOneField(
        User,
        'соглашение'
    )

    class Meta:
        verbose_name = 'соглашение пользователя'
        verbose_name_plural = 'соглашения пользователя'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'agreement'),
                name='unique_agreement'
            )
        )

    def __str__(self):
        return self.user[:TRUNCATED_NAME]


class Expertise(models.Model):
    """ Направление разработки. """

    name = models.CharField(
        'Название',
        max_length=MAX_WORKPLACE_CHARS,
        unique=True
    )

    class Meta:
        verbose_name = 'направление'
        verbose_name_plural = 'направления'

    def __str__(self):
        return self.name[:TRUNCATED_NAME]


class Stack(models.Model):
    """ Стек. """

    name = models.CharField(
        'Название',
        max_length=MAX_WORKPLACE_CHARS,
        unique=True
    )
    expertise = models.ForeignKey(
        Expertise,
        'Направление',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'стек'
        verbose_name_plural = 'стек'

    def __str__(self):
        return self.name[:TRUNCATED_NAME]


class UserExpertise(models.Model):
    """ Связь пользователь-направление-стек. """

    user = models.ForeignKey(
        User,
        'Пользователь',
        on_delete=models.CASCADE)
    expertise = models.ForeignKey(
        Expertise,
        'Направление',
        on_delete=models.CASCADE)
    stack = models.ForeignKey(
        Stack,
        'Стек',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'направление и стек пользователя'
        verbose_name_plural = 'направления и стек пользователя'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'expertise'),
                name='unique_expertise'
            )
        )

    def __str__(self):
        return f' Направление и стек пользователя {self.user[:TRUNCATED_NAME]}'
