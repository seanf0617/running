# Generated by Django 4.0.4 on 2022-05-20 11:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_rename_distance_recordactivity_recorddistance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recordactivity',
            old_name='recorddate',
            new_name='date',
        ),
        migrations.AddField(
            model_name='recordactivity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recordactivity',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='recordactivity',
            name='username',
            field=models.CharField(max_length=150, null=True),
        ),
    ]