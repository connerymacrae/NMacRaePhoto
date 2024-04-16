# Generated by Django 4.2.9 on 2024-04-16 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('biography', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('date_taken', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='photos')),
                ('tag', models.CharField(blank=True, choices=[('e', 'Event'), ('w', 'Wedding'), ('o', 'Outdoor'), ('h', 'Headshot'), ('p', 'Product'), ('a', 'Art')], max_length=6)),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='photomanager.photographer')),
            ],
        ),
    ]
