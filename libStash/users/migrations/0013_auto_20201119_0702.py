# Generated by Django 3.1.1 on 2020-11-19 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_delete_bookreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='account',
        ),
        migrations.DeleteModel(
            name='BookInCart',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
