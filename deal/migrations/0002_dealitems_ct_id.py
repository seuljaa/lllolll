# Generated by Django 4.0.1 on 2022-02-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealitems',
            name='ct_id',
            field=models.PositiveIntegerField(default=8, verbose_name='content_type_id'),
        ),
    ]