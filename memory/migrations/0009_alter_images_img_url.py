# Generated by Django 4.1.6 on 2023-02-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0008_alter_images_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img_url',
            field=models.ImageField(upload_to=''),
        ),
    ]
