from django.urls import path
from . import views

app_name = 'receptionist'
urlpatterns = [
    path('',views.index, name='index'),
    path('view_all_appointments', views.view_all_appointments, name='view_all_appointments'),
    path('view_all_appointments/<int:ap_id>/edit_appointment', views.edit_appointment, name='edit_appointment'),
    path('view_all_appointments/<int:ap_id>/edit_appointment/delete_appointment', views.delete_appointment, name='delete_appointment'), 
    path('view_all_appointments/<int:ap_id>/after_deletion', views.after_deletion, name='after_deletion'),     
    path('create_new_appointment', views.createAppointment, name='create_new_appointment'),
    path('view_all_patients', views.view_all_patients, name='view_all_patients'),
    path('view_all_patients/<int:patient_id>/invoice_history', views.view_invoice_history, name='view_invoice_history'),
    path('view_all_patients/<int:patient_id>/invoice_history/<int:invoice_id>/edit_invoice', views.edit_invoice, name='edit_invoice'),
    path('view_all_patients/<int:patient_id>/invoice_history/<int:invoice_id>/edit_invoice/delete_invoice', views.delete_invoice, name='delete_invoice'),
    path('view_all_patients/<int:patient_id>/invoice_history/<int:invoice_id>/after_deletion_invoice', views.after_deletion_invoice, name='after_deletion_invoice'),
    path('view_all_patients/<int:patient_id>/create_invoice', views.create_invoice, name='create_invoice'),   
    path('create_new_patient', views.createPatient, name='create_new_patient'),
    path('view_all_patients/<int:p_id>/edit_patient', views.edit_patient, name='edit_patient'),
    path('view_all_patients/<int:p_id>/edit_patient/delete_patient', views.delete_patient, name='delete_patient'),
    path('view_all_patients/<int:p_id>/after_deletion_patient', views.after_deletion_patient, name='after_deletion_patient'),       
]