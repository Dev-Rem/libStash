# Generated by Django 3.0.4 on 2021-04-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0026_auto_20210409_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='State'),
        ),
    ]
