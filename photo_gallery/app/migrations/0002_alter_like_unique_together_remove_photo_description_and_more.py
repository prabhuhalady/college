# Generated by Django 5.0.6 on 2024-06-07 15:02

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='photo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='like',
            name='session_key',
            field=models.CharField(default=uuid.uuid4, max_length=40),
        ),
        migrations.AddField(
            model_name='photo',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='like',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
    ]
