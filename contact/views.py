from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

from .models import Contact


class ContactListView(ListView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'contact/contact_create.html'


class ContactDetailView(DetailView):
    model = Contact


class ContactUpdateView(UpdateView):
    model = Contact
    fields = '__all__'


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('cotact:email_list')
