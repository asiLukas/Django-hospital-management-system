# Generated by Django 3.0.8 on 2020-07-12 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='patient_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cases.Patient'),
        ),
    ]
