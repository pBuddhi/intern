from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Guest(models.Model):
    first_name = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="invalid")
    phone_number = models.CharField(validators=[phone_regex], blank=True,max_length=15)
    def __str__(self):
        return self.first_name

class Enquiry(models.Model):
    requirement = models.ForeignKey(Guest,null=True)
    need = models.CharField(max_length=200)
    def __str__(self):
        return self.need

class DatabaseInsert(models.Model):
    username = models.CharField(max_length=200)
    phone_reg = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="invalid")
    phone = models.CharField(validators=[phone_reg], blank=True,max_length=15)
    def __str__(self):
        return self.username

class Requirement(models.Model):
    mehman = models.ForeignKey(DatabaseInsert,null=True)
    query = models.CharField(max_length=200)    
    def __str__(self):
        return self.query
