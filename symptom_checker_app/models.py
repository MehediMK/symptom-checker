from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Symptom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Disease(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.ManyToManyField(Symptom)

    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialties = models.ManyToManyField('Disease', related_name='doctors')

    def __str__(self):
        return self.name

    