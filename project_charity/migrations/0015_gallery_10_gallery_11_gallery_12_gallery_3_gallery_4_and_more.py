# Generated by Django 4.2.3 on 2023-07-22 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_charity', '0014_gallery_2_rename_gallery_gallery_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery_10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название картинки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='help_cases/')),
            ],
            options={
                'verbose_name': 'Картинки галлереи 10',
                'verbose_name_plural': 'Картинки галлереи 10',
            },
        ),
        migrations.CreateModel(
            name='Gallery_11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название картинки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='help_cases/')),
            ],
            options={
                'verbose_name': 'Картинки галлереи 11',
                'verbose_name_plural': 'Картинки галлереи 11',
            },
        ),
        migrations.CreateModel(
            name='Gallery_12',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название картинки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='help_cases/')),
            ],
            options={
                'verbose_name': 'Картинки галлереи 12',
                'verbose_name_plural': 'Картинки галлереи 12',
            },
        ),
        migrations.CreateModel(
            name='Gallery_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название картинки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='help_cases/')),
            ],
            options={
                'verbose_name': 'Картинки галлереи 3',
                'verbose_name_plural': 'Картинки галлереи 3',
            },
        ),
        migrations.CreateModel(
            name='Gallery_4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название картинки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='help_cases/')),
            ],
            options={
                'verbose_name': 'Картинки галлереи 4',
                'verbose_name_plural': 'Картинки галлереи 4',
            },
        ),
        migrations.CreateModel(
            name='Gallery_5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название картинки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='help_cases/')),
            ],
            options={
                'verbose_name': 'Картинки галлереи 5',
                'verbose_name_plural': 'Картинки галлереи 5',
            },
        ),
        migrations.CreateModel(
            name='Gallery_6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название картинки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='help_cases/')),
            ],
            options={
                'verbose_name': 'Картинки галлереи 6',
                'verbose_name_plural': 'Картинки галлереи 6',
            },
        ),
        migrations.CreateModel(
            name='Gallery_7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название картинки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='help_cases/')),
            ],
            options={
                'verbose_name': 'Картинки галлереи 7',
                'verbose_name_plural': 'Картинки галлереи 7',
            },
        ),
        migrations.CreateModel(
            name='Gallery_8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название картинки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='help_cases/')),
            ],
            options={
                'verbose_name': 'Картинки галлереи 8',
                'verbose_name_plural': 'Картинки галлереи 8',
            },
        ),
        migrations.CreateModel(
            name='Gallery_9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название картинки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='help_cases/')),
            ],
            options={
                'verbose_name': 'Картинки галлереи 9',
                'verbose_name_plural': 'Картинки галлереи 9',
            },
        ),
    ]