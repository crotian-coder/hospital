from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Address(models.Model):
	line1 = models.CharField(max_length=100,default="")
	city = models.CharField(max_length=100,default="")
	state = models.CharField(max_length=50,default="")
	pincode = models.CharField(max_length=6,default="")




DOCTOR_SPEACIALITIES = (
	("General","general"),
	("Orthopedics","orthopedics"),
	("Internal Medicine","internal medicine."),
	("Gynecology", "gynecology"),
	("Dermatology","dermatology"),
	("Pediatrics","pediatrics"),
	("Radiology","radiology"),
	("General Surgery","general surgery")
	)


PATIENT_BLOOD_GROUPS = (
	("A+","A+"),
	("A-","A-"),
	("B+","B+"),
	("B-","B-"),
	("O+","O+"),
	("O-","O-"),
	("AB-","AB-"),
	("AB+","AB+"),
	)

APPOINTMENT_STATUS = (
	('Pending','pending'),
	('Confirmed','confirmed'),
	('Rejected','rejected')
	)

class Doctor(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="doctor")
	speaciality = models.CharField(max_length=100,choices = DOCTOR_SPEACIALITIES,default = "General")
	

class Patient(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	blood_group = models.CharField(max_length=10,choices = PATIENT_BLOOD_GROUPS)

class Appointment(models.Model):
	doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	description = models.TextField(default="")
	status = models.CharField(max_length=20,choices=APPOINTMENT_STATUS ,default="Pending")
	

class Test(models.Model):
	name = models.CharField(max_length=100)
	number = models.IntegerField()




