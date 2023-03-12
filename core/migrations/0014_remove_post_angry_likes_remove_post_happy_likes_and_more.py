# Generated by Django 4.1.7 on 2023-03-12 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_suprisedreact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='angry_likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='happy_likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='sad_likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='shocked_likes',
        ),
        migrations.AddField(
            model_name='suprisedreact',
            name='reacts',
            field=models.IntegerField(default=0),
        ),
    ]