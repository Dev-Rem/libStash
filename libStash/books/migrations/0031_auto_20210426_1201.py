# Generated by Django 3.0.4 on 2021-04-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0030_auto_20210426_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('THR', 'Thriller'), ('FNSY', 'Fantasy'), ('RMCE', 'Romance'), ('AVTRE', 'Adventure')], max_length=10, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='format',
            field=models.CharField(choices=[('E-BK', 'E-Book'), ('HD-CVR', 'Hardcover'), ('PPR-BCK', 'Paperback')], max_length=10, verbose_name='Format'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Title'),
        ),
    ]
