# Generated by Django 3.2.8 on 2021-11-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20211104_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='video',
        ),
        migrations.AddField(
            model_name='question',
            name='video_id',
            field=models.IntegerField(default=0),
        ),
    ]
