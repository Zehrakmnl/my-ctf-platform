# Generated by Django 5.0.1 on 2024-04-18 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscore',
            name='dateTime',
            field=models.DateTimeField(default=None),
        ),
    ]
