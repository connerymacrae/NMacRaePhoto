# Generated by Django 4.2.9 on 2024-05-15 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photomanager', '0004_phototag_remove_photo_date_taken_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 15, 18, 33, 55, 901563, tzinfo=datetime.timezone.utc)),
        ),
    ]
