# Generated by Django 4.0.1 on 2022-02-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ct_id',
            field=models.PositiveIntegerField(default=12, verbose_name='content_type_id'),
        ),
    ]