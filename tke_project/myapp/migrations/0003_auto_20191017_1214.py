# Generated by Django 2.2.6 on 2019-10-17 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20191017_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_date',
            field=models.DateField(default='2019-10-17'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='published_date',
            field=models.DateField(default='2019-05-17'),
            preserve_default=False,
        ),
    ]