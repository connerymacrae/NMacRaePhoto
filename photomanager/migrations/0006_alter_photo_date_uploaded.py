# Generated by Django 4.2.9 on 2024-05-15 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photomanager', '0005_alter_photo_date_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_uploaded',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
