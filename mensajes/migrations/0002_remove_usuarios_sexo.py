# Generated by Django 4.1.4 on 2022-12-26 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='sexo',
        ),
    ]
