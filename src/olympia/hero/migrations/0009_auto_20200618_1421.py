# Generated by Django 2.2.12 on 2020-06-18 14:21

from django.db import migrations, models
import olympia.hero.models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0008_auto_20200616_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryheroimage',
            name='custom_image',
            field=models.ImageField(blank=True, upload_to='hero-featured-image/'),
        ),
    ]
