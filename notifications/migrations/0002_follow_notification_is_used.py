# Generated by Django 3.0.2 on 2020-02-05 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow_notification',
            name='is_used',
            field=models.IntegerField(default=0),
        ),
    ]