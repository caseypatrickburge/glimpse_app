# Generated by Django 2.2.7 on 2020-01-24 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='api',
            old_name='descrption',
            new_name='description',
        ),
    ]