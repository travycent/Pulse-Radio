# Generated by Django 3.2.2 on 2021-05-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtnpulseapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dj',
            name='dj_website',
            field=models.URLField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
