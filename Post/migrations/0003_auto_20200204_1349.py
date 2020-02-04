# Generated by Django 2.2 on 2020-02-04 13:49

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20200204_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='pictureContent',
        ),
        migrations.AddField(
            model_name='card',
            name='picture',
            field=versatileimagefield.fields.VersatileImageField(default='images/default_avatar.png', upload_to='images', verbose_name='pictureContent'),
        ),
    ]
