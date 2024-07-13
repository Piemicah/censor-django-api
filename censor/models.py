from django.db import models


class Persons(models.Model):
    fname = models.CharField(max_length=150)
    sname = models.CharField(max_length=150)
    mname = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    lga = models.CharField(max_length=100, blank=True, null=True)
    nin = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    address = models.CharField(max_length=150, blank=True, null=True)
    picture = models.CharField(max_length=200, blank=True, null=True)
