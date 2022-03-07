# Generated by Django 4.0.1 on 2022-03-07 15:48

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
            name='Main_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgfile', models.ImageField(upload_to='photo')),
            ],
        ),
        migrations.CreateModel(
            name='Photo_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='갱신날짜')),
                ('content', models.TextField()),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('ct_id', models.PositiveIntegerField(default=10, verbose_name='content_type_id')),
                ('likes_user', models.ManyToManyField(blank=True, related_name='likes_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo_like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('ct_id', models.PositiveIntegerField(default=10, verbose_name='content_type_id')),
                ('likes_user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.photo_post')),
            ],
        ),
        migrations.CreateModel(
            name='Photo_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgfile', models.ImageField(upload_to='photo')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.photo_post')),
            ],
        ),
    ]
