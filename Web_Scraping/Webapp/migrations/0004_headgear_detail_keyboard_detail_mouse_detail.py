# Generated by Django 4.0.3 on 2022-03-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0003_headgear_keyboard_banana_keyboard_brand_keyboard_jib_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='headgear',
            name='Detail',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AddField(
            model_name='keyboard',
            name='Detail',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AddField(
            model_name='mouse',
            name='Detail',
            field=models.CharField(default='None', max_length=500),
        ),
    ]
