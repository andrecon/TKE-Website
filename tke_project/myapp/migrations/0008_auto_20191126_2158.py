# Generated by Django 2.2.6 on 2019-11-26 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='state',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]