from django import forms
from .models import Donate, Appointment

class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ('name','email','mobile','bloodgroup','sex','age','address')

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('name','email','mobile','sex','age','timing','specialist')
