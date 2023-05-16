# Generated by Django 3.2.16 on 2023-02-05 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_search_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='nat',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='neg',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='pos',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.login'),
        ),
    ]
