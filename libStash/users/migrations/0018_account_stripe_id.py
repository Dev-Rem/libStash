# Generated by Django 3.1.1 on 2020-12-20 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_account_stripe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
