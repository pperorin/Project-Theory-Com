# Generated by Django 4.0.3 on 2022-04-07 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0008_alter_headgear_banana_alter_headgear_ihavecpu_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headgear',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='keyboard',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='mouse',
            name='Price',
        ),
    ]
