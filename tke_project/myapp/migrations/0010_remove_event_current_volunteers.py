# Generated by Django 2.2.6 on 2019-12-03 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20191127_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='current_volunteers',
        ),
    ]
