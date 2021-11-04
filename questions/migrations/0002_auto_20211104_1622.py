# Generated by Django 3.2.8 on 2021-11-04 16:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_video_videofile'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.video'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
        ),
    ]