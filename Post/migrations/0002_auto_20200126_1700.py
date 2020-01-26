# Generated by Django 3.0.2 on 2020-01-26 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Post.Card'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='card',
            name='voteDown',
        ),
        migrations.AddField(
            model_name='card',
            name='voteDown',
            field=models.ManyToManyField(related_name='voteDown', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='card',
            name='voteUp',
        ),
        migrations.AddField(
            model_name='card',
            name='voteUp',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='children',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.Comment'),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='voteDown',
        ),
        migrations.AddField(
            model_name='comment',
            name='voteDown',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='voteUp',
        ),
        migrations.AddField(
            model_name='comment',
            name='voteUp',
            field=models.ManyToManyField(related_name='voteUp', to=settings.AUTH_USER_MODEL),
        ),
    ]
