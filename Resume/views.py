from django.shortcuts import render

from .forms import *


# Create your views here.

def index(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request, 'accept.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})
