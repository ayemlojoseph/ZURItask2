from django import forms



# forms.forms dont need class Meta, this only applies to Model forms
#and why would your contact form be referencing a Profile model?.. You need to think harder
"""
class ContactForm(forms.Form):
    class Meta:
        model = Profile
        fields = (
            'name', 'phone_number', 'email', 'address', 'objective', 'educational_background',
            'professional_experience',
            'skills')
"""
#Here is a new one
class ContactForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={
       'placeholder': 'Enter Email',
       'class': 'form-control'
    }))
    subject = forms.CharField(max_length=100, widget=forms.Textarea(attrs={
       'placeholder': 'Write message',
       'class': 'form-control'
    }))
    message = forms.CharField(max_length=100, widget=forms.Textarea(attrs={
       'placeholder': 'Write message',
       'class': 'form-control'
    }))
