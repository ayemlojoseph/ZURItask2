from django.contrib import admin

# Register your models here.
from .models import Profile

admin.site.register(Profile)


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')
