# Generated by Django 3.0.8 on 2020-07-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0003_case_patient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='done',
            field=models.BooleanField(null=True),
        ),
    ]
