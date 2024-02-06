from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    no_of_employees = models.PositiveIntegerField()

    def __str__(self):
        return self.name
