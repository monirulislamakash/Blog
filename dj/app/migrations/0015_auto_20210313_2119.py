# Generated by Django 3.1.2 on 2021-03-13 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210306_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 13, 21, 19, 17, 279788)),
        ),
    ]
