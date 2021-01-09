from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:patient_id>', views.view_patient, name='view_patient'),
    path('<int:patient_id>/appointments', views.view_appointment, name='view_appointment'),
    path('<int:patient_id>/profile', views.view_profile, name='view_profile'),
    path('<int:patient_id>/view_med_hist', views.view_med_hist, name='view_med_hist'),
    path('<int:patient_id>/view_invoices', views.view_invoices, name='view_invoices'),
]