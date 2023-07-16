# Generated by Django 4.2.3 on 2023-07-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_charity', '0006_helpcase'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpcase',
            name='address_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='helpcase',
            name='address_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='helpcase',
            name='description_full_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='helpcase',
            name='description_full_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='helpcase',
            name='description_title_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='helpcase',
            name='description_title_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='helpcase',
            name='title_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Название случая'),
        ),
        migrations.AddField(
            model_name='helpcase',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Название случая'),
        ),
    ]