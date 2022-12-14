# Generated by Django 4.1.3 on 2022-11-17 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0005_alter_movie_date_alter_music_content_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movie', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='music_content',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='music', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
