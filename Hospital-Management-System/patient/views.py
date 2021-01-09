from django.shortcuts import render
from .models import Patient, MedicalHistory, invoice
from receptionist.models import Appointments

# Create your views here.
def index(request):
    return render(request, 'patient/index.html',{
        'patients': Patient.objects.all()
    })

def view_patient(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    return render(request, 'patient/view_patient.html',{
        'patient': patient
    })

def view_appointment(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    appointments = Appointments.objects.filter(patient = patient)
    return render(request, 'patient/view_appoint.html',{
        'patient': patient, 'appointments': appointments
    })

def view_profile(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    return render(request, 'patient/view_profile.html',{
        'patient': patient
    })

def view_med_hist(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    medHist = MedicalHistory.objects.filter(patient=patient)
    return render(request, 'patient/view_med_hist.html',{
        'medHist': medHist
    })

def view_invoices(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    invoices = invoice.objects.filter(patient=patient)
    return render(request, 'patient/view_invoice.html',{
        'invoices': invoices
    })