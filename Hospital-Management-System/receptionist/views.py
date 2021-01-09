from django.shortcuts import render
from .models import Appointments, AppointmentForm, InvoiceForm
from patient.models import Patient, PatientForm, invoice

# Create your views here.
def index(request):
    total_appoint = Appointments.objects.count()
    done_appoint = Appointments.objects.filter(status='Completed').count()
    upcoming_appoint = total_appoint - done_appoint
    return render(request,'receptionist/recep_home.html',{
        'total_appoint':total_appoint, 'done_appoint':done_appoint, 'upcoming_appoint':upcoming_appoint
    })


#                                   APPOINTMENTS

def view_all_appointments(request):
    return render(request, 'receptionist/view_appointments.html',{
        'appointments': Appointments.objects.all()
    })

def view_all_patients(request):
    return render(request, 'receptionist/view_patients.html',{
        'patients': Patient.objects.all()
    })

def createAppointment(request):
    if request.method == 'POST':
        appointmentForm = AppointmentForm(request.POST)
        if appointmentForm.is_valid():
            appointmentForm.save()
            return render(request,'receptionist/view_appointments.html',{
                    'appointments': Appointments.objects.all()
            })
        else:
            return render(request, 'receptionist/create_appoint.html',{
                'appointForm': AppointmentForm(),'error':"Error"
            })

    return render(request, 'receptionist/create_appoint.html',{
        'appointmentForm': AppointmentForm()
    })


    
def edit_appointment(request, ap_id):
    appointment = Appointments.objects.get(pk=ap_id)
    ap_form = AppointmentForm(instance=appointment)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return render(request,'receptionist/view_appointments.html',{
                'appointments': Appointments.objects.all()
            })
        else:
            return render(request,'receptionist/edit_appointment.html',{
                'ap':appointment, 'ap_form':ap_form, 'error':'Please edit again'
            })

    return render(request,'receptionist/edit_appointment.html',{
        'ap':appointment, 'ap_form':ap_form
    })

def delete_appointment(request,ap_id):
    ap = Appointments.objects.get(pk=ap_id)
    return render(request,'receptionist/delete_appointment.html',{
        'ap':ap
    })

def after_deletion(request,ap_id):
    Appointments.objects.filter(pk=ap_id).delete()
    return render(request,'receptionist/view_appointments.html',{
                'appointments': Appointments.objects.all()
            }) 


#                                   PATIENT

def createPatient(request):
    if request.method == 'POST':
        patientForm = PatientForm(request.POST)
        if patientForm.is_valid():
            patientForm.save()
            return render(request,'receptionist/view_patients.html',{
                    'patients': Patient.objects.all()
            })
        else:
            return render(request, 'receptionist/create_patient.html',{
                'patientForm': PatientForm(),'error':"Error"
            })

    return render(request, 'receptionist/create_patient.html',{
        'patientForm': PatientForm()
    })


def edit_patient(request, p_id):
    patient = Patient.objects.get(pk=p_id)
    p_form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return render(request,'receptionist/view_patients.html',{
                'patients': Patient.objects.all()
            })
        else:
            return render(request,'receptionist/edit_patient.html',{
                'p':patient, 'p_form':p_form, 'error':'Please edit again'
            })

    return render(request,'receptionist/edit_patient.html',{
        'p':patient, 'p_form':p_form
    })

def delete_patient(request,p_id):
    p = Patient.objects.get(pk=p_id)
    return render(request,'receptionist/delete_patient.html',{
        'p':p
    })

def after_deletion_patient(request,p_id):
    Patient.objects.filter(pk=p_id).delete()
    return render(request,'receptionist/view_patients.html',{
                'patients': Patient.objects.all()
            })



                                # PATIENT INVOICE

def view_invoice_history(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    patient_invoice = invoice.objects.filter(patient=patient)
    return render(request, 'receptionist/view_patient_invoice.html',{
        'patient':patient, 'invoice':patient_invoice
    })

def create_invoice(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'receptionist/view_patient_invoice.html',{
                'patient':patient, 'invoice':invoice.objects.filter(patient=patient)
            })
        else:
            return render(request, 'receptionist/create_invoice.html',{
                'patient':patient, 'invoiceForm':InvoiceForm(initial={'patient':patient}), 'error':"Please try again"
            })

    return render(request, 'receptionist/create_invoice.html',{
        'patient':patient, 'invoiceForm':InvoiceForm(initial={'patient':patient})
    })

def edit_invoice(request,patient_id,invoice_id):
    i = invoice.objects.get(pk=invoice_id)
    i_form = InvoiceForm(instance=i)
    patient = Patient.objects.get(pk=patient_id)

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=i)
        if form.is_valid():
            form.save()
            return render(request,'receptionist/view_patient_invoice.html',{
                'patient':patient, 'invoice':invoice.objects.filter(patient=patient)
            })
        else:
            return render(request,'receptionist/edit_invoice.html',{
                'i':i, 'i_form':i_form, 'error':'Please edit again', 'patient':patient
            })

    return render(request,'receptionist/edit_invoice.html',{
        'i':i, 'i_form':i_form, 'patient':patient
    })

def delete_invoice(request,patient_id,invoice_id):
    i = invoice.objects.get(pk=invoice_id)
    patient = Patient.objects.get(pk=patient_id)
    return render(request,'receptionist/delete_invoice.html',{
        'i':i, 'patient':patient
    })

def after_deletion_invoice(request,patient_id, invoice_id):
    invoice.objects.filter(pk=invoice_id).delete()
    patient = Patient.objects.get(pk=patient_id)
    return render(request,'receptionist/view_patient_invoice.html',{
                'patient':patient, 'invoice':invoice.objects.filter(patient=patient)
            })