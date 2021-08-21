from django import forms
from .models import *


class ContactForm(forms.Form):
    class Meta:
        model = Profile
        fields = (
            'name', 'phone_number', 'email', 'address', 'objective', 'educational_background',
            'professional_experience',
            'skills')
