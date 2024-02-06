from django.db import models
from organization.models import Organization  # Import the Organization model

class Employee(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    date_joined = models.DateField()

    def __str__(self):
        return self.name