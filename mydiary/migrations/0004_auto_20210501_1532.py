# Generated by Django 3.1.7 on 2021-05-01 06:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0003_auto_20210501_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='star',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
