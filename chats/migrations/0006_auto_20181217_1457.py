# Generated by Django 2.1.2 on 2018-12-17 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0005_auto_20181217_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 17, 14, 57, 30, 774249)),
        ),
    ]