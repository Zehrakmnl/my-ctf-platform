# Generated by Django 5.0.1 on 2024-03-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0010_item_correctansw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='correctAnsw',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
