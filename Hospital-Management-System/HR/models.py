from django.db import models

# Create your models here.
class HR(models.Model):
    username = models.CharField(max_length=10)
    # password = models.CharField(max_length=10)

    def __str__(self):
        return self.username