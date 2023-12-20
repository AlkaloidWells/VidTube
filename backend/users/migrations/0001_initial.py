# Generated by Django 4.2.1 on 2023-12-20 02:06

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
            name='Vidtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('robohash_set', models.IntegerField(default=3)),
                ('user_summary', models.CharField(default='I think my arm is on backward.', max_length=300)),
                ('user_location', models.CharField(default='Hell, Earth', max_length=100)),
                ('open_search_new_tab', models.BooleanField(default=True)),
                ('enable_gradient_bg', models.BooleanField(default=False)),
                ('hide_unavailable_videos', models.BooleanField(default=True)),
                ('confirm_before_deleting', models.BooleanField(default=True)),
                ('show_import_page', models.BooleanField(default=True)),
                ('yt_channel_id', models.TextField(default='')),
                ('import_in_progress', models.BooleanField(default=False)),
                ('imported_yt_playlists', models.BooleanField(default=False)),
                ('access_token', models.TextField(default='')),
                ('refresh_token', models.TextField(default='')),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
                ('manage_playlists_import_textarea', models.TextField(default='')),
                ('create_playlist_name', models.CharField(default='', max_length=50)),
                ('create_playlist_desc', models.CharField(default='', max_length=50)),
                ('create_playlist_type', models.CharField(default='', max_length=50)),
                ('create_playlist_add_vids_from_collection', models.CharField(default='', max_length=50)),
                ('create_playlist_add_vids_from_links', models.CharField(default='', max_length=50)),
                ('vidtube_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
