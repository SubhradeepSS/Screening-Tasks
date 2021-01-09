from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name