# Generated by Django 4.0.1 on 2022-01-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]