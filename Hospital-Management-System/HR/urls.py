from django.urls import path
from . import views

app_name = 'HR'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_doctor', views.add_doctor, name='add_doctor'),
    path('view_doctors', views.view_doctors, name='view_doctors'),
    path('view_doctors/<int:dr_id>/edit_profile', views.edit_profile, name='edit_profile'), 
    path('view_doctors/<int:dr_id>/edit_profile/delete_profile', views.delete_profile, name='delete_profile'),
    path('view_doctors/<int:dr_id>/after_deletion', views.after_deletion, name='after_deletion')     
]