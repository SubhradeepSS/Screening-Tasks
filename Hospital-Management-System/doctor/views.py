from django.shortcuts import render
from receptionist.models import Appointments
from .models import Doctor
from patient.models import MedicalHistory,Create_Prescription

# Create your views here.
def index(request):
    return render(request, 'doctor/index.html',{
        'doctors': Doctor.objects.all()
    })

def view_doctor(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    return render(request, 'doctor/view_doctor.html',{
        'doctor': doctor
    })

def view_profile(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    return render(request, 'doctor/view_profile.html',{
        'doctor': doctor
    })

def view_appointment(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    appointments = Appointments.objects.filter(doctor = doctor, status="Pending")
    return render(request, 'doctor/view_appoint.html',{
        'doctor': doctor, 'appointments': appointments
    })

def view_prescriptions(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    prescriptions = MedicalHistory.objects.filter(doctor=doctor)
    return render(request, 'doctor/view_prescriptions.html',{
        'prescriptions': prescriptions,'doctor':doctor
    })

def create_prescription(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)

    if request.method == 'POST':
        prescriptionForm = Create_Prescription(request.POST)
        if prescriptionForm.is_valid():
            data = prescriptionForm.cleaned_data
            patient = data['patient']
            date = data['date']
            symptoms = data['symptoms']
            prescription = data['prescription']
            m = MedicalHistory(doctor=doctor,patient=patient,symptoms=symptoms,prescription=prescription,date=date)
            m.save()
            return render(request, 'doctor/view_prescriptions.html',{
                'prescriptions': MedicalHistory.objects.filter(doctor=doctor),'doctor':doctor
            })
        else:
            return render(request, 'doctor/create_prescription.html',{
                'prescription_form': Create_Prescription(),'error':"Error",'doctor':doctor
            })

    return render(request, 'doctor/create_prescription.html',{
        'prescription_form': Create_Prescription(),'doctor':doctor
    })

def edit_prescription(request,doctor_id,prescription_id):
    p = MedicalHistory.objects.get(pk=prescription_id)
    p_form = Create_Prescription(instance=p)
    doctor = Doctor.objects.get(pk=doctor_id)

    if request.method == 'POST':
        form = Create_Prescription(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return render(request,'doctor/view_prescriptions.html',{
                'prescriptions': MedicalHistory.objects.filter(doctor=doctor),'doctor':doctor
            })
        else:
            return render(request,'doctor/edit_prescription.html',{
                'p':p, 'p_form':p_form, 'error':'Please edit again', 'doctor':doctor
            })

    return render(request,'doctor/edit_prescription.html',{
        'p':p, 'p_form':p_form, 'doctor':doctor
    })

def delete_prescription(request,doctor_id,prescription_id):
    p = MedicalHistory.objects.get(pk=prescription_id)
    doctor = Doctor.objects.get(pk=doctor_id)
    return render(request,'doctor/delete_prescription.html',{
        'p':p, 'doctor':doctor
    })

def after_deletion(request,doctor_id, prescription_id):
    MedicalHistory.objects.filter(pk=prescription_id).delete()
    doctor = Doctor.objects.get(pk=doctor_id)
    return render(request,'doctor/view_prescriptions.html',{
                'prescriptions': MedicalHistory.objects.filter(doctor=doctor),'doctor':doctor
            })