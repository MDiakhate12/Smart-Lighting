# Generated by Django 2.2.2 on 2019-07-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_meeting_doing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='static/images/anonym.png', upload_to=''),
        ),
    ]
