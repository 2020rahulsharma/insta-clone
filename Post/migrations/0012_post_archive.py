# Generated by Django 3.1.1 on 2020-09-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0011_remove_post_save'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
