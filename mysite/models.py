from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Donate(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField()
    mobile = PhoneNumberField()
    bloodgroup_choices = (('apos', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        )
    bloodgroup = models.CharField(choices=bloodgroup_choices, max_length=5 ,blank=True)
    SEX_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
        ('Transgender', 'Transgender',),
    )
    sex = models.CharField(
        max_length=15,
        choices=SEX_CHOICES,
    )
    age = models.IntegerField()
    address = models.CharField(max_length=80, default='')

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField()
    mobile = PhoneNumberField()
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('T', 'Transgender',),
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )
    age = models.IntegerField()
    TIMING_CHOICES = (
        ('Morn', '10 AM - 1 PM',),
        ('Aft', '2 PM - 5 PM',),
        ('Eve', '6 PM - 9 PM',),
    )
    timing = models.CharField(
        max_length=4,
        choices=TIMING_CHOICES,
    )
    Specialist_CHOICES = (
        ('car','Cardiologist',),
        ('pl','Plastic Surgeon',),
        ('psy','Psychiatrist',),
        ('rad','Radiologist',),
        ('sur','Surgeon',),
    )
    specialist = models.CharField(
        max_length=20,
        choices=Specialist_CHOICES,
    )
