# Generated by Django 4.1.7 on 2023-03-11 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_comment_comment_id_alter_post_post_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.CharField(default='95B75A42F9', editable=False, max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(default='9493153AE2', editable=False, max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_user',
            field=models.CharField(default='B016DBCB42', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]
