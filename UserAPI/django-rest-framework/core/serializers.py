from rest_framework import serializers
from .models import *

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ('lat', 'lng')


class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer()
    class Meta:
        model = Address
        fields = ('street', 'city', 'suite', 'zipcode', 'geo')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'catchPhrase', 'bs')


class UserSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    address = AddressSerializer()
    class Meta:
        model = User
        fields = ('user_id','name', 'username', 'phone', 'email', 'website', 'address', 'company')