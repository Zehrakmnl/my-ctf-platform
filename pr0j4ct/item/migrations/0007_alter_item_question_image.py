# Generated by Django 5.0.1 on 2024-03-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_alter_item_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='question_image',
            field=models.ImageField(blank=True, default='/Users/zehra/Desktop/ALL Project/Django/Task HackTime/pr0j4ct/static/images/tis.png', upload_to='item_images'),
        ),
    ]
