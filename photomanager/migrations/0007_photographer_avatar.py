# Generated by Django 4.2.9 on 2024-05-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photomanager', '0006_alter_photo_date_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='avatar',
            field=models.ImageField(default='photos/photos/photographers/null.png', upload_to='photos/photographers'),
        ),
    ]
