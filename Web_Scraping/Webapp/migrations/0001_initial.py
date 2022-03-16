# Generated by Django 4.0.2 on 2022-03-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('KeyboardId', models.AutoField(primary_key=True, serialize=False)),
                ('KeyboardName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('MouseId', models.AutoField(primary_key=True, serialize=False)),
                ('MouseName', models.CharField(max_length=500)),
            ],
        ),
    ]
