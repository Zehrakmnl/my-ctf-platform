# Generated by Django 5.0.1 on 2024-06-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0016_alter_data_file_alter_item_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='file',
            field=models.FileField(blank=True, max_length=500, null=True, upload_to='static/file/'),
        ),
    ]
