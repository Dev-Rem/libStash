# Generated by Django 3.0.4 on 2021-04-07 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_account_stripe_id'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='account',
            table='account',
        ),
        migrations.AlterModelTable(
            name='address',
            table='address',
        ),
    ]
