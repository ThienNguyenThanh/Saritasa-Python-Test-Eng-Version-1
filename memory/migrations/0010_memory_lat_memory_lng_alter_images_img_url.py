# Generated by Django 4.1.6 on 2023-02-12 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0009_alter_images_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='memory',
            name='lng',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='images',
            name='img_url',
            field=models.ImageField(upload_to='', verbose_name='Images'),
        ),
    ]
