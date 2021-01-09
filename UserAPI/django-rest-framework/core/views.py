from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework import generics

import requests

URL = "https://jsonplaceholder.typicode.com/users"

# Create your views here.
def index(request):
    response = requests.get(URL)
    data = response.json()

    for user in data:
        geo = Geo.objects.create(
            lat=user['address']['geo']['lat'], lng=user['address']['geo']['lng']
            )

        company = Company.objects.create(
            name=user['company']['name'], catchPhrase=user['company']['catchPhrase'], bs=user['company']['bs']
            )

        address = Address.objects.create(
            street=user['address']['street'], suite=user['address']['suite'], city=user['address']['city'],
            zipcode=user['address']['zipcode'], geo=geo
            )

        User.objects.create(
            user_id=user['id'], name=user['name'], username=user['username'], email=user['email'], phone=user['phone'],
            website=user['website'], address=address, company=company
        )
        
    message = { 'Response': 'Successfully added users to database' }
    return JsonResponse(data=message)


class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        self.queryset.delete()
        return self.list(request, *args, **kwargs)


class UserView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    lookup_field = 'user_id'
    serializer_class = UserSerializer