# Generated by Django 5.0.1 on 2024-04-18 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0011_alter_item_correctansw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]