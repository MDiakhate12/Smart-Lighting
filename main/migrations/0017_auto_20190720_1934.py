# Generated by Django 2.2.2 on 2019-07-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20190720_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='main/static/images/anonym.png', upload_to=''),
        ),
    ]