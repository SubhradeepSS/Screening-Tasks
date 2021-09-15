from .serializers import ContactSerializer
from .models import Contact
from rest_framework import generics


# Create your views here.
class ContactsView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class SearchNameView(generics.ListAPIView):
    lookup_url_kwarg = 'name'
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(name__contains=self.kwargs.get(self.lookup_url_kwarg))


class SearchEmailView(generics.ListAPIView):
    lookup_url_kwarg = 'email'
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(email=self.kwargs.get(self.lookup_url_kwarg))
