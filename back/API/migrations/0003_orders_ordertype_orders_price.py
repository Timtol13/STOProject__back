# Generated by Django 4.1.8 on 2023-05-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_orders_user_services_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='orderType',
            field=models.CharField(blank=True, max_length=255, verbose_name='Order Type'),
        ),
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.IntegerField(blank=True, default=1, verbose_name='Price'),
            preserve_default=False,
        ),
    ]
