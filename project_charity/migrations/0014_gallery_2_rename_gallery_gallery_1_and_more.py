# Generated by Django 4.2.3 on 2023-07-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_charity', '0013_alter_gallery_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название картинки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='help_cases/')),
            ],
            options={
                'verbose_name': 'Картинки галлереи 2',
                'verbose_name_plural': 'Картинки галлереи 2',
            },
        ),
        migrations.RenameModel(
            old_name='Gallery',
            new_name='Gallery_1',
        ),
        migrations.AlterModelOptions(
            name='gallery_1',
            options={'verbose_name': 'Картинки галлереи 1', 'verbose_name_plural': 'Картинки галлереи 1'},
        ),
    ]