# Generated by Django 2.2.6 on 2019-11-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanners', '0013_auto_20191105_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scannerrule',
            name='action',
            field=models.PositiveSmallIntegerField(choices=[(1, 'No action'), (20, 'Flag for human review'), (100, 'Delay auto-approval'), (200, 'Delay auto-approval indefinitely')], default=1),
        ),
    ]
