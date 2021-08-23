from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Contact
from django.contrib import messages

# Create your views here.

# Remember you created your form wrogly, thus you wont expect to get any output
# on the screen
"""
def index(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request, 'accept.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})
"""


# Sending the contact form to database
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("The form is valid")
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            subject = form.cleaned_data.get('subject')
            contact = Contact(email=email, subject=subject, message=message)
            contact.save()
            messages.info(request, "Message Sent, Thank you for contacting me...")
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})


