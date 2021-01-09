from django.db import models
from doctor.models import Doctor
from patient.models import Patient, invoice
from django.forms import ModelForm
# Create your models here.

STATUS = (
    ("Pending","Pending"), ("Completed","Completed")
)

class Appointments(models.Model):
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices= STATUS, default='Pending', max_length=10)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'Appointment ID: {self.id}'

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointments
        fields = ['date', 'time', 'status', 'doctor', 'patient']

class InvoiceForm(ModelForm):
    class Meta:
        model = invoice
        fields = ['date', 'paid', 'outstanding', 'patient']