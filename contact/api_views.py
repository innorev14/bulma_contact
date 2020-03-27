from rest_framework import generics
from .serializers import ContactSerializer
from .models import Contact

class ContactAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer