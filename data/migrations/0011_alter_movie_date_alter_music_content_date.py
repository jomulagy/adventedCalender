# Generated by Django 4.2.6 on 2023-10-21 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_alter_movie_date_alter_music_content_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='music_content',
            name='date',
            field=models.DateField(),
        ),
    ]
