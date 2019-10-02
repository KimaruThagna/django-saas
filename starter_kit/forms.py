from django import forms
from .models import *
from django.contrib.auth.models import User

class PatientRecordForm(forms.ModelForm):
    class Meta:
        model = PatientData
        exclude = ['lastUpdated','addedOn','processed','addedBy','requestingPractitioner','diagnosis','requestDate','requestNumber']

    def save(self, commit=True):
        patient = super(PatientRecordForm, self).save(commit=False)
        if commit:
            patient.save()
        return patient
