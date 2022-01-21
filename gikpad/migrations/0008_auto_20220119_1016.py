# Generated by Django 3.2.4 on 2022-01-19 07:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gikpad', '0007_auto_20220119_1014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='caption',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='clientrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 19, 7, 16, 46, 187292, tzinfo=utc)),
        ),
    ]
