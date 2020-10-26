# Generated by Django 3.1.1 on 2020-10-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20200925_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='phone',
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='publisher',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
    ]