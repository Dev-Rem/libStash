# Generated by Django 3.0.4 on 2021-04-07 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20210407_0913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcomment',
            options={},
        ),
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
        migrations.AlterModelTable(
            name='postcomment',
            table='post_comment',
        ),
        migrations.AlterModelTable(
            name='postimage',
            table='post_image',
        ),
    ]
