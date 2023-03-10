# Generated by Django 4.1.7 on 2023-03-10 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_profile_id_user_post_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.UUIDField(unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.UUIDField(unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_user',
            field=models.UUIDField(unique=True),
        ),
    ]
