# Generated by Django 5.0.3 on 2024-04-10 15:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(unique=True, verbose_name='текст соглашения')),
                ('is_required', models.BooleanField(verbose_name='обязательное/необязательное соглашение')),
            ],
            options={
                'verbose_name': 'соглашение',
                'verbose_name_plural': 'соглашения',
            },
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'направление',
                'verbose_name_plural': 'направления',
                'default_related_name': 'expertises',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('last_name',), 'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='employment',
            field=models.CharField(max_length=100, null=True, verbose_name='Место работы'),
        ),
        migrations.AddField(
            model_name='user',
            name='experience',
            field=models.CharField(choices=[('NO_EXP', 'Нет опыта'), ('ONE_YEAR', 'От 1 года'), ('THREE_YEARS', 'От 3 лет'), ('FIVE_YEARS', 'От 5 лет')], max_length=255, null=True, verbose_name='Опыт работы'),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile_number',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(max_length=100, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='user',
            name='preferred_format',
            field=models.CharField(choices=[('OFFLINE', 'Оффлайн'), ('ONLINE', 'Онлайн')], max_length=255, null=True, verbose_name='Предпочитаемый формат'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='Фамилия'),
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('expertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.expertise', verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'стек',
                'verbose_name_plural': 'стек',
                'default_related_name': 'stack_items',
            },
        ),
        migrations.CreateModel(
            name='UserAgreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_signed', models.BooleanField(null=True, verbose_name='cостояние соглашения')),
                ('agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.agreement', verbose_name='соглашение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'соглашение пользователя',
                'verbose_name_plural': 'соглашения пользователя',
                'default_related_name': 'agreements',
            },
        ),
        migrations.CreateModel(
            name='UserExpertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.expertise', verbose_name='Направление')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'направление пользователя',
                'verbose_name_plural': 'направления пользователя',
                'default_related_name': 'user_expertise',
            },
        ),
        migrations.AddConstraint(
            model_name='useragreement',
            constraint=models.UniqueConstraint(fields=('user', 'agreement'), name='unique_agreement'),
        ),
        migrations.AddConstraint(
            model_name='userexpertise',
            constraint=models.UniqueConstraint(fields=('user', 'expertise'), name='unique_expertise'),
        ),
    ]