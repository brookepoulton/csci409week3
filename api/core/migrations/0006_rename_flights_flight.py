# Generated by Django 5.0.1 on 2024-02-08 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_flights_origin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Flights',
            new_name='Flight',
        ),
    ]
