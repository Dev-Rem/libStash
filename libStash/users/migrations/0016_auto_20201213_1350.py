# Generated by Django 3.1.1 on 2020-12-13 13:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_account_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL),
        ),
    ]
