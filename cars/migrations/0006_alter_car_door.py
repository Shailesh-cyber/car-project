# Generated by Django 4.0.2 on 2022-02-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='door',
            field=models.IntegerField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10),
        ),
    ]