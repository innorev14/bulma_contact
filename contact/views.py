from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

from .models import Contact


class ContactListView(ListView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    template_name = 'contact/contact_create.html'


class ContactDetailView(DetailView):
    model = Contact


class ContactUpdateView(UpdateView):
    model = Contact


class ContactDeleteView(DeleteView):
    model = Contact
