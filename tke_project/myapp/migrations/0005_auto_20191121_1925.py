# Generated by Django 2.2.6 on 2019-11-21 19:25

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rush'),
    ]

    operations = [
        migrations.AddField(
            model_name='rush',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default=0, max_length=128, region=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rush',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rush',
            name='lastName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rush',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rush',
            name='year',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]
