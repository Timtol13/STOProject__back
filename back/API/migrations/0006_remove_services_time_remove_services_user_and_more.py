# Generated by Django 4.1.8 on 2023-05-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_orders_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='time',
        ),
        migrations.RemoveField(
            model_name='services',
            name='user',
        ),
        migrations.AddField(
            model_name='services',
            name='image',
            field=models.FileField(default=1, upload_to=None, verbose_name='Icon'),
            preserve_default=False,
        ),
    ]
