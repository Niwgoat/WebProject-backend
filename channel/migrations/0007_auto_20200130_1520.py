# Generated by Django 3.0.2 on 2020-01-30 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0006_merge_20200130_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='picture',
            field=models.ImageField(default='images/AI_HW1.png', upload_to='images'),
        ),
    ]