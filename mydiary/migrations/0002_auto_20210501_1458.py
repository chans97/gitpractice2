# Generated by Django 3.1.7 on 2021-05-01 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='body',
        ),
        migrations.AddField(
            model_name='content',
            name='highlight',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.ImageField(null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='content',
            name='review',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='star',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='user',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]