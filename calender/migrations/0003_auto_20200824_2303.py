# Generated by Django 3.0.2 on 2020-08-24 14:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0002_auto_20200824_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 24, 19, 33, 33, 897082, tzinfo=utc), verbose_name='수정일'),
        ),
    ]
