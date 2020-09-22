# Generated by Django 3.1.1 on 2020-09-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200920_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='warehousebook',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]