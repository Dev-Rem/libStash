# Generated by Django 3.1.1 on 2020-10-27 20:53

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201026_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='unique_id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='address',
            name='unique_id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='bookincart',
            name='unique_id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='bookreview',
            name='unique_id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='unique_id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
    ]
