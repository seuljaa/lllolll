# Generated by Django 4.0.1 on 2022-01-24 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deal', '0001_initial'),
        ('photo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True, null=True)),
                ('deal_items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deal.dealitems')),
                ('photo_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.photo_post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
