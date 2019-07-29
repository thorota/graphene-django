from django.db import models
from django.utils import timezone

class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
       return self.name

# Create your models here.
