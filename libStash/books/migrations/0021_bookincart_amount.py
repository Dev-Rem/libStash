# Generated by Django 3.1.1 on 2020-12-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0020_auto_20201219_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookincart',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Book unit amount'),
        ),
    ]