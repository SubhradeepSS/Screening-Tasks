from django.contrib import admin
from .models import Patient, MedicalHistory, invoice

# Register your models here.
admin.site.register(Patient)
admin.site.register(MedicalHistory)
admin.site.register(invoice)