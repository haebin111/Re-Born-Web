# Generated by Django 3.0.2 on 2020-02-26 09:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0003_auto_20200226_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 26, 14, 51, 53, 694368, tzinfo=utc), verbose_name='수정일'),
        ),
    ]