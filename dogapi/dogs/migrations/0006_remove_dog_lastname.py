# Generated by Django 4.2.6 on 2023-10-11 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0005_dog_lastname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='Lastname',
        ),
    ]
