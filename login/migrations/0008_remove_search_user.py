# Generated by Django 3.2.16 on 2023-02-05 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20230205_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='user',
        ),
    ]
