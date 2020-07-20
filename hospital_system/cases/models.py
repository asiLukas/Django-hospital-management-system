from django.db import models
from django.urls import reverse
import django.utils.timezone
from django.contrib.auth.models import User


class Patient(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('cases:patient_detail', kwargs={'id': self.id})


class Case(models.Model):
    case = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateField(default=django.utils.timezone.now)
    patient_name = models.ForeignKey(Patient, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.case

    def get_absolute_url(self):
        return reverse('cases:detail', kwargs={'id': self.id})
