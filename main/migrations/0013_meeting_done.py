# Generated by Django 2.2.2 on 2019-07-18 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_meeting_chatroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
