# Generated by Django 4.1.6 on 2023-02-10 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('comment', models.TextField()),
                ('img_url', models.TextField()),
            ],
        ),
    ]
