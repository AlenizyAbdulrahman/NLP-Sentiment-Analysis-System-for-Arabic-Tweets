# Generated by Django 3.2.16 on 2023-02-06 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_remove_search_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='is_Manager',
        ),
        migrations.AddField(
            model_name='search',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.login'),
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]