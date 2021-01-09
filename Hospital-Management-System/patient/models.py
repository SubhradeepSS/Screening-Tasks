from django.db import models
from django.forms import ModelForm
from doctor.models import Doctor
from django.contrib.auth.models import AbstractUser

# Create your models here.
GENDER = (
    ("Male","Male"), ("Female","Female"), ("Other", "Other")
)

BLOOD_GROUPS = (
    ('A+','A+'), ('A-','A-'), ('B+','B+'), ('AB-', 'AB-'), ('O+','O+'), ('B-','B-'), ('O-','O-'), ('AB+','AB+')
)

class Patient(models.Model):
    username = models.CharField(max_length=100)
    # password = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(choices= GENDER, max_length=10)
    age = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=500)
    blood_group = models.CharField(choices= BLOOD_GROUPS, max_length=4)


    def __str__(self):
        return self.name

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        # exclude = ['password']

class invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    paid = models.IntegerField()
    date = models.DateField()
    outstanding = models.IntegerField()

    def __str__(self):
        return f'ID: {self.id}; Date: {self.date}; Paid: {self.paid}; Outstanding: {self.outstanding}'

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    symptoms = models.CharField(max_length=100)
    prescription = models.CharField(max_length=500)

    def __str__(self):
        return f'Date: {self.date}; Symptoms: {self.symptoms}; Prescription: {self.prescription}; Patient: {self.patient}; Doctor: {self.doctor}'

class Create_Prescription(ModelForm):
    class Meta:
        model = MedicalHistory
        fields = '__all__'
        exclude = ['doctor']