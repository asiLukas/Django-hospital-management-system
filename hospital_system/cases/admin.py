from django.contrib import admin
from .models import Case, Patient
# Register your models here.

admin.site.register(Patient)
admin.site.register(Case)
