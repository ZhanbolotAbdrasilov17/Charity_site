# Generated by Django 4.2.3 on 2023-07-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_charity', '0017_rename_slider1_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('text_ru', models.TextField(null=True)),
                ('text_ky', models.TextField(null=True)),
                ('text_en', models.TextField(null=True)),
                ('low_text', models.TextField()),
                ('low_text_ru', models.TextField(null=True)),
                ('low_text_ky', models.TextField(null=True)),
                ('low_text_en', models.TextField(null=True)),
                ('inner_text', models.TextField()),
                ('inner_text_ru', models.TextField(null=True)),
                ('inner_text_ky', models.TextField(null=True)),
                ('inner_text_en', models.TextField(null=True)),
                ('website', models.URLField()),
            ],
            options={
                'verbose_name': 'Описание в главной странице',
                'verbose_name_plural': 'Описание в главной странице',
            },
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'Слайдер', 'verbose_name_plural': 'Слайдер'},
        ),
    ]
