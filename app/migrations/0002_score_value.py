# Generated by Django 2.2.6 on 2019-10-03 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
