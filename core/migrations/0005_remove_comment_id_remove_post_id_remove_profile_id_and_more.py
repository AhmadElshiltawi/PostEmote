# Generated by Django 4.1.7 on 2023-03-10 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_profile_bio_alter_comment_comment_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.CharField(default='EDEE0', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(default='AFD44', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_user',
            field=models.CharField(default='A8DC3', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]