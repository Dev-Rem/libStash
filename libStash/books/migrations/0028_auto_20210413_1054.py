# Generated by Django 3.0.4 on 2021-04-13 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0027_auto_20210411_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehousebook',
            name='book',
        ),
        migrations.RemoveField(
            model_name='warehousebook',
            name='warehouse',
        ),
        migrations.DeleteModel(
            name='Warehouse',
        ),
        migrations.DeleteModel(
            name='WarehouseBook',
        ),
    ]