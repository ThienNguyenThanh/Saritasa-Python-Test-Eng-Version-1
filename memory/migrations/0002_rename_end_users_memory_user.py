# Generated by Django 4.1.6 on 2023-02-10 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memory',
            old_name='end_users',
            new_name='user',
        ),
    ]
