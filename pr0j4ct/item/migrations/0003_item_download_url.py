# Generated by Django 5.0.1 on 2024-03-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='download_url',
            field=models.URLField(default=''),
        ),
    ]