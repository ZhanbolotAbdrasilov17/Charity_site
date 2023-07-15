# Generated by Django 4.2.3 on 2023-07-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_charity', '0004_about_us_mainpaig'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('address', models.CharField(max_length=200, verbose_name='Почта клиентов')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Почтовые адреса',
                'verbose_name_plural': 'Почтовые адреса',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название партнёра')),
                ('image', models.ImageField(blank=True, null=True, upload_to='partner-image', verbose_name='Логотип партнера')),
            ],
            options={
                'verbose_name': 'Партнёр',
                'verbose_name_plural': 'Партнёры',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.CharField(max_length=200, verbose_name='Инстаграм')),
                ('whatsapp', models.CharField(max_length=200, verbose_name='Ватсап')),
                ('facebook', models.CharField(max_length=200, verbose_name='Фейсбук')),
                ('vk', models.CharField(blank=True, max_length=200, null=True, verbose_name='Вконтакте')),
                ('twitter', models.CharField(blank=True, max_length=200, null=True, verbose_name='Твиттер')),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
    ]