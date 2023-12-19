from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50, null=False) 
    last_name  = models.CharField(max_length=50) 
    email = models.EmailField(max_length=254) 
    country = CountryField()
    date_of_joining = models.DateField()
    relieving_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pass