# Generated by Django 3.1.1 on 2020-10-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='comment',
            field=models.CharField(max_length=500, null=True, verbose_name='Comment'),
        ),
    ]
