# Generated by Django 4.1.7 on 2023-03-20 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_post_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='angry_reaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.angryreact'),
        ),
        migrations.AddField(
            model_name='comment',
            name='happy_reaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.happyreact'),
        ),
        migrations.AddField(
            model_name='comment',
            name='sad_reaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.sadreact'),
        ),
        migrations.AddField(
            model_name='comment',
            name='surprised_reaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.suprisedreact'),
        ),
    ]
