# Generated by Django 4.0.2 on 2022-02-21 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_fuel_type_alter_car_is_featured'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Car',
        ),
    ]
