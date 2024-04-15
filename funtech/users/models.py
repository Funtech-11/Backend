# from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
from django.db import models
from events.enums import EventTypeEnum, ExperienceEnum

GENERAL_MAX_LENGTH_LIMIT = 255
MAX_WORKPLACE_CHARS = 100
TRUNCATED_NAME = 10


class User(AbstractUser):

    REQUIRED_FIELDS = ('first_name',
                       'last_name',
                       'password',
                       'email')
    USERNAME_FIELD = 'username'

    first_name = models.CharField(
        'Имя',
        max_length=GENERAL_MAX_LENGTH_LIMIT
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=GENERAL_MAX_LENGTH_LIMIT
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=GENERAL_MAX_LENGTH_LIMIT,
        unique=True,
    )
    mobile_number = models.PositiveSmallIntegerField(null=True)  # валидация формата? +7(111)111-11-11
    photo = models.ImageField(blank=True, null=True)
    employment = models.CharField(
        'Место работы',
        max_length=MAX_WORKPLACE_CHARS,
        null=True
    )
    position = models.CharField(
        'Должность',
        max_length=MAX_WORKPLACE_CHARS,
        null=True
    )
    experience = models.CharField(
        verbose_name='Опыт работы',
        max_length=GENERAL_MAX_LENGTH_LIMIT,
        choices=[
            (exp_type.name, exp_type.value) for exp_type in ExperienceEnum
        ],
        null=True
    )
    preferred_format = models.CharField(
        verbose_name='Предпочитаемый формат',
        max_length=GENERAL_MAX_LENGTH_LIMIT,
        choices=[
            (event_type.name, event_type.value) for event_type in EventTypeEnum
        ],
        null=True
    )

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Agreement(models.Model):
    """ Соглашение. Создается админом. """

    text = models.TextField(
        'текст соглашения',
        unique=True
    )
    is_required = models.BooleanField(
        'отметка обязательное/необязательное'
    )

    class Meta:
        verbose_name = 'соглашение'
        verbose_name_plural = 'соглашения'

    def __str__(self):
        return self.text[:TRUNCATED_NAME]


class UserAgreement(models.Model):
    """ Соглашение пользователя. """

    agreement = models.ForeignKey(
        Agreement,
        verbose_name='соглашение',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        on_delete=models.CASCADE
    )
    is_signed = models.BooleanField(
        'cостояние соглашения',
        null=True
    )

    class Meta:
        verbose_name = 'соглашение пользователя'
        verbose_name_plural = 'соглашения пользователя'
        default_related_name = 'user_agreements'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'agreement'),
                name='unique_agreement'
            ),
        )

    def __str__(self):
        return (f'Соглашение {self.agreement.id} пользователя '
                f'{self.user.first_name} {self.user.last_name}')


class Expertise(models.Model):
    """ Направление разработки. """

    name = models.CharField(
        'Название',
        max_length=MAX_WORKPLACE_CHARS,
        unique=True
    )
    stacks = models.ManyToManyField('Stack',
                                    through='UserExpertise')

    class Meta:
        verbose_name = 'направление'
        verbose_name_plural = 'направления'
        default_related_name = 'expertises'

    def __str__(self):
        return self.name[:TRUNCATED_NAME]


class Stack(models.Model):
    """ Стек. """

    name = models.CharField(
        'Название',
        max_length=MAX_WORKPLACE_CHARS,
    )

    class Meta:
        verbose_name = 'стек'
        verbose_name_plural = 'стек'
        default_related_name = 'stack_items'

#    def __str__(self):
#        return self.name[:TRUNCATED_NAME]


class UserExpertise(models.Model):
    """ Связь пользователь-направление. """

    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='userExper')
    expertise = models.ForeignKey(
        Expertise,
        verbose_name='Направление',
        on_delete=models.CASCADE,
        related_name='Exper')
    stack = models.ForeignKey(Stack,
                              on_delete=models.CASCADE,
                              blank=True)

    class Meta:
        verbose_name = 'направление пользователя'
        verbose_name_plural = 'направления пользователя'
#        constraints = (
#            models.UniqueConstraint(
#                fields=('user', 'expertise', 'stack'),
#                name='unique_expertise'
#            ),
#        )

#    def __str__(self):
#        return f' Направление и стек пользователя {self.user[:TRUNCATED_NAME]}'
