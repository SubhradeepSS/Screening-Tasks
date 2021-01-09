from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:doctor_id>', views.view_doctor, name='view_doctor'),
    path('<int:doctor_id>/profile', views.view_profile, name='view_profile'),
    path('<int:doctor_id>/appointments', views.view_appointment, name='view_appointment'),
    path('<int:doctor_id>/prescriptions', views.view_prescriptions, name='view_prescriptions'),
    path('<int:doctor_id>/create_prescription', views.create_prescription, name='create_prescription'),
    path('<int:doctor_id>/prescriptions/<int:prescription_id>/edit_prescription', views.edit_prescription, name='edit_prescription'),
    path('<int:doctor_id>/prescriptions/<int:prescription_id>/edit_prescription/delete_prescription', views.delete_prescription, name='delete_prescription'),
    path('<int:doctor_id>/prescriptions/<int:prescription_id>/after_deletion', views.after_deletion, name='after_deletion')     
]