from django.db import models

# Create your models here.
class Geo(models.Model):
    lat = models.DecimalField(decimal_places=4, max_digits=10)
    lng = models.DecimalField(decimal_places=4, max_digits=10)


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    suite = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=15)
    geo = models.ForeignKey(Geo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.suite}, zipcode: {self.zipcode}, latitude: {self.geo.lat}, longitude: {self.geo.lng}"


class Company(models.Model):
    name = models.CharField(max_length=20)
    catchPhrase = models.CharField(max_length=100)
    bs = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name