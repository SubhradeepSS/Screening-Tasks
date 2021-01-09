from django.db import models
from django.forms import ModelForm

# Create your models here.
GENDER = (
    ("Male","Male"), ("Female","Female"), ("Other", "Other")
)

STATUS = (
    ("Active","Active"), ("Not Active","Not Active")
)

class Doctor(models.Model):
    username = models.CharField(max_length=100)
    # password = models.CharField(max_length=10)
    name =  models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(choices= GENDER, max_length=10)
    department = models.CharField(max_length=10)
    attendance = models.IntegerField()
    salary = models.IntegerField()
    status = models.CharField(choices= STATUS, default='Not Active', max_length=10)

    def __str__(self):
        return self.name

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        # exclude = ['password']