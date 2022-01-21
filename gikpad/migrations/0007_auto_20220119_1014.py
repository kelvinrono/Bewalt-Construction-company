# Generated by Django 3.2.4 on 2022-01-19 07:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gikpad', '0006_auto_20220116_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'galleries'},
        ),
        migrations.RenameField(
            model_name='gallery',
            old_name='location',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='clientrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 19, 7, 14, 23, 815356, tzinfo=utc)),
        ),
    ]
