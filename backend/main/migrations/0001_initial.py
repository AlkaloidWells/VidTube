# Generated by Django 3.2.6 on 2021-12-04 01:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.TextField(blank=True)),
                ('channel_name', models.TextField(blank=True)),
                ('is_yt_mix', models.BooleanField(default=False)),
                ('playlist_id', models.CharField(max_length=150)),
                ('name', models.CharField(blank=True, max_length=150)),
                ('thumbnail_url', models.TextField(blank=True)),
                ('description', models.TextField(default='No description')),
                ('video_count', models.IntegerField(default=0)),
                ('published_at', models.DateTimeField(blank=True)),
                ('is_private_on_yt', models.BooleanField(default=False)),
                ('playlist_yt_player_HTML', models.TextField(blank=True)),
                ('playlist_duration', models.CharField(blank=True, max_length=69)),
                ('playlist_duration_in_seconds', models.IntegerField(default=0)),
                ('started_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_watched', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_notes', models.TextField(default='')),
                ('user_label', models.CharField(default='', max_length=100)),
                ('marked_as', models.CharField(default='none', max_length=100)),
                ('is_favorite', models.BooleanField(blank=True, default=False)),
                ('num_of_accesses', models.IntegerField(default='0')),
                ('last_accessed_on', models.DateTimeField(default=datetime.datetime.now)),
                ('is_user_owned', models.BooleanField(default=True)),
                ('auto_check_for_updates', models.BooleanField(default=False)),
                ('is_in_db', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_full_scan_at', models.DateTimeField(auto_now_add=True)),
                ('has_playlist_changed', models.BooleanField(default=False)),
                ('has_new_updates', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=100)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('duration', models.CharField(blank=True, max_length=100)),
                ('duration_in_seconds', models.IntegerField(default=0)),
                ('thumbnail_url', models.TextField(blank=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(default='')),
                ('has_cc', models.BooleanField(blank=True, default=False, null=True)),
                ('liked', models.BooleanField(default=False)),
                ('public_stats_viewable', models.BooleanField(default=True)),
                ('view_count', models.IntegerField(default=0)),
                ('like_count', models.IntegerField(default=0)),
                ('dislike_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('yt_player_HTML', models.TextField(blank=True)),
                ('channel_id', models.TextField(blank=True)),
                ('channel_name', models.TextField(blank=True)),
                ('is_unavailable_on_yt', models.BooleanField(default=False)),
                ('was_deleted_on_yt', models.BooleanField(default=False)),
                ('is_planned_to_watch', models.BooleanField(default=False)),
                ('is_marked_as_watched', models.BooleanField(default=False)),
                ('is_favorite', models.BooleanField(blank=True, default=False)),
                ('num_of_accesses', models.IntegerField(default=0)),
                ('user_label', models.CharField(blank=True, max_length=100)),
                ('user_notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('video_details_modified', models.BooleanField(default=False)),
                ('video_details_modified_at', models.DateTimeField(auto_now_add=True)),
                (
                    'untube_user',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='videos',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=69)),
                ('times_viewed', models.IntegerField(default=0)),
                ('times_viewed_per_week', models.IntegerField(default=0)),
                ('last_views_reset', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'created_by',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='playlist_tags',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_item_id', models.CharField(max_length=100)),
                ('video_position', models.IntegerField(blank=True)),
                ('published_at', models.DateTimeField(default=datetime.datetime.now)),
                ('channel_id', models.CharField(max_length=250, null=True)),
                ('channel_name', models.CharField(max_length=250, null=True)),
                ('is_duplicate', models.BooleanField(default=False)),
                ('is_marked_as_watched', models.BooleanField(blank=True, default=False)),
                ('num_of_accesses', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'playlist',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='playlist_items',
                        to='main.playlist'
                    )
                ),
                ('video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.video')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='tags',
            field=models.ManyToManyField(related_name='playlists', to='main.Tag'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='untube_user',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='playlists',
                to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name='playlist',
            name='videos',
            field=models.ManyToManyField(related_name='playlists', to='main.Video'),
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=100)),
                (
                    'playlist',
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.playlist')
                ),
                (
                    'untube_user',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='pins',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
                ('video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.video')),
            ],
        ),
    ]
