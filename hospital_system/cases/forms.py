from .models import Case, Patient
from django import forms
from django.utils import timezone


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'first_name', 'last_name', 'address', 'email'
        ]


class CaseForm(forms.ModelForm):
    created = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': 'example: 2020-6-7'
    }), initial=timezone.now())

    class Meta:
        model = Case
        fields = [
            'case', 'description', 'created', 'patient_name', 'finished'
        ]
