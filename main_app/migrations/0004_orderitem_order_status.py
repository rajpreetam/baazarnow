# Generated by Django 4.0.3 on 2022-05-23 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order_status',
            field=models.BooleanField(default=False),
        ),
    ]
