# Generated by Django 3.2.2 on 2021-09-03 15:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mixtapes', '0005_alter_djmixtape_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='dj',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
