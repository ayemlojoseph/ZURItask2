from django.db import models


# Create your models here.

#What do you need a profile model for?
"""
class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    objective = models.TextField()
    educational_background = models.TextField()
    professional_experience = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return self.name
"""
#Where do you intend to save the information when user contacts you?
#you need a contact model to save the form response in the database

class Contact (models.Model):
    email = models.EmailField(max_length=255, null=True, blank=True)
    subject = models.TextField(max_length=255, null=True, blank=True)
    message = models.TextField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.email)

