# Generated by Django 4.0.3 on 2022-05-23 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_order_status_orderitem_order_complete_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_complete_status',
            field=models.BooleanField(default=False),
        ),
    ]