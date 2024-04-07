# Generated by Django 5.0.3 on 2024-04-06 20:00

import django.core.validators
import django.db.models.deletion
import events.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
                ('builing', models.CharField(max_length=255, verbose_name='Строение')),
                ('metro_station', models.CharField(blank=True, max_length=255, verbose_name='Станция метро')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('speaker_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('job', models.CharField(max_length=255, verbose_name='Позиция')),
                ('avatar', models.ImageField(null=True, upload_to=events.models.get_upload_speaker_avatar_path, verbose_name='Аватар')),
            ],
            options={
                'verbose_name': 'Докладчик',
                'verbose_name_plural': 'Докладчики',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('theme_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тематика',
                'verbose_name_plural': 'Тематики',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('date_time', models.DateTimeField(null=True, verbose_name='Дата и время')),
                ('number_of_participants', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Число участников')),
                ('information', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('event_type', models.CharField(choices=[('Оффлайн', 'OFFLINE'), ('Онлайн', 'ONLINE')], max_length=255, verbose_name='Тип')),
                ('event_format', models.CharField(blank=True, choices=[('CONFERENCE', 'Конференция'), ('MEETUP', 'Митап'), ('NETWORKING', 'Нетворкинг'), ('EXCURSION', 'Экскурсия')], max_length=255, verbose_name='Формат')),
                ('status', models.CharField(choices=[('REGISTRATION_OPEN', 'Регистрация открыта'), ('REGISTRATION_CLOSE', 'Регистрация закрыта'), ('FINISHED', 'Завершено')], max_length=255, verbose_name='Статус')),
                ('activity_status', models.CharField(choices=[('DRAFT', 'Черновик'), ('ACTIVE_EVENT', 'Активное мероприятие')], max_length=255, verbose_name='Состояние')),
                ('wallpaper', models.ImageField(null=True, upload_to=events.models.get_upload_wallpaper_path, verbose_name='Фото')),
                ('video', models.URLField(verbose_name='Ссылка на видеозапись')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='events.location')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='events.theme')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('program_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('date_time', models.DateTimeField(null=True, verbose_name='Дата и время')),
                ('information', models.TextField(max_length=1000, verbose_name='Описание')),
                ('material', models.FileField(upload_to=events.models.get_upload_material_path, verbose_name='Файл')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='events.event')),
                ('speaker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='programs', to='events.speaker')),
            ],
            options={
                'verbose_name': 'Программа',
                'verbose_name_plural': 'Программы',
            },
        ),
    ]