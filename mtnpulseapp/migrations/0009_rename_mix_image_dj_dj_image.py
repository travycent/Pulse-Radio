# Generated by Django 3.2.2 on 2021-05-11 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtnpulseapp', '0008_dj_mix_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dj',
            old_name='mix_image',
            new_name='dj_image',
        ),
    ]
