# Generated by Django 2.1.7 on 2019-04-05 08:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190405_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutorialseries',
            options={'verbose_name_plural': 'Tutorial Series'},
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 5, 16, 52, 49, 683834), verbose_name='date published'),
        ),
    ]
