# Generated by Django 3.1.1 on 2020-09-21 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0009_auto_20200921_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='archive',
        ),
    ]