# Generated by Django 4.2.9 on 2024-05-15 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photomanager', '0003_alter_photo_photographer_alter_photo_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='date_taken',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='location',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='photographer',
        ),
        migrations.AddField(
            model_name='photo',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.date(2024, 5, 15)),
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.RemoveField(
            model_name='photo',
            name='tag',
        ),
        migrations.AddField(
            model_name='photo',
            name='tag',
            field=models.ManyToManyField(to='photomanager.phototag'),
        ),
    ]
