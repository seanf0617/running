# Generated by Django 4.0.4 on 2022-05-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordactivity',
            name='recorddate',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
