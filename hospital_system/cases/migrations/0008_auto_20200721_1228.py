# Generated by Django 3.0.8 on 2020-07-21 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0007_auto_20200721_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='date',
            new_name='created',
        ),
    ]
