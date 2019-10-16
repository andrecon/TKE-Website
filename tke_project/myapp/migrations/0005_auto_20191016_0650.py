# Generated by Django 2.2.6 on 2019-10-16 06:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20191016_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='current_volunteers',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event',
            name='max_volunteers',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]