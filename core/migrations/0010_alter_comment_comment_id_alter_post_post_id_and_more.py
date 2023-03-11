# Generated by Django 4.1.7 on 2023-03-11 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_comment_comment_id_alter_post_post_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.CharField(default='448D5DA6A4', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(default='4F2E8F9900', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_user',
            field=models.CharField(default='899817A973', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]
