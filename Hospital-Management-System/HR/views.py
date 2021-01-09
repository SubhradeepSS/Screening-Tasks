from django.shortcuts import render
from doctor.models import Doctor, DoctorForm
from patient.models import Patient

# Create your views here.
def index(request):
    total_doc = Doctor.objects.count()
    onduty_doc = Doctor.objects.filter(status='Active').count()
    total_patients = Patient.objects.count()
    return render(request, 'HR/index.html',{
       'total_doc':total_doc, 'onduty_doc':onduty_doc, 'total_patients':total_patients
    })

def view_doctors(request):
    return render(request,'HR/view_doctors.html',{
        'doctorsDB': Doctor.objects.all()
    })

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            # data = form.cleaned_data
            # username = data['username']
            # name = data['name']
            # phone = data['phone']
            # email = data['email']
            # gender = data['gender']
            # department = data['department']
            # attendance = data['attendance']
            # salary = data['salary']
            # status = data['status']
            # d = Doctor(username=username,name=name,phone=phone,email=email,gender=gender,department=department,attendance=attendance,salary=salary,status=status)
            form.save()
            return render(request,'HR/view_doctors.html',{
                'doctorsDB': Doctor.objects.all()
            })
        else:
            return render(request,'HR/add_dr.html',{
                'doctorForm': DoctorForm(), 'message': "Please try again"
            }) 

    return render(request,'HR/add_dr.html',{
        'doctorForm': DoctorForm()
    })
    
    
def edit_profile(request, dr_id):
    doctor = Doctor.objects.get(pk=dr_id)
    dr_form = DoctorForm(instance=doctor)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            # data = form.cleaned_data
            # doctor.username = data['username']
            # doctor.name = data['name']
            # doctor.phone = data['phone']
            # doctor.email = data['email']
            # doctor.gender = data['gender']
            # doctor.department = data['department']
            # doctor.attendance = data['attendance']
            # doctor.salary = data['salary']
            # doctor.status = data['status']
            form.save()
            return render(request,'HR/view_doctors.html',{
                'doctorsDB': Doctor.objects.all()
            })
        else:
            return render(request,'HR/edit_dr.html',{
                'dr':doctor, 'dr_form':dr_form, 'error':'Please edit again'
            })

    return render(request,'HR/edit_dr.html',{
        'dr':doctor, 'dr_form':dr_form
    })

def delete_profile(request,dr_id):
    dr = Doctor.objects.get(pk=dr_id)
    return render(request,'HR/delete_profile.html',{
        'dr':dr
    })

def after_deletion(request,dr_id):
    Doctor.objects.filter(pk=dr_id).delete()
    return render(request,'HR/view_doctors.html',{
                'doctorsDB': Doctor.objects.all()
            }) 