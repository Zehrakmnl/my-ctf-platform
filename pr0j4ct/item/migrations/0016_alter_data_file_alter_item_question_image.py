# Generated by Django 5.0.1 on 2024-06-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0015_alter_item_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='file',
            field=models.FileField(blank=True, upload_to='static/file/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
