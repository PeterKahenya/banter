# Generated by Django 2.1.2 on 2018-12-17 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_message_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Sent at'),
        ),
    ]
