# Generated by Django 4.1.3 on 2022-11-03 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0003_alter_song_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recode', models.FileField(upload_to='voice_record')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voice_likes', models.ManyToManyField(related_name='like_voice', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'voice',
                'ordering': ['-created_at'],
            },
        ),
    ]
