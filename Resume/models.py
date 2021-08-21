from django.db import models


# Create your models here.
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
