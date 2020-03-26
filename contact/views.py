from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

from .forms import ContactForm
from .models import Contact


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = Contact.objects.all()
        query = self.request.GET.get("qs", None)
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ContactListView, self).get_context_data(*args, **kwargs)
        return context

class ContactCreateView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'contact/contact_create.html'
    success_url = reverse_lazy('contact:email_create')


class ContactDetailView(DetailView):
    model = Contact


class ContactUpdateView(UpdateView):
    model = Contact
    fields = '__all__'


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact:email_list')


def email_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone_no']
            service = form.cleaned_data['service']
            url_type = form.cleaned_data['url_type']
            url = form.cleaned_data['url']
            content = form.cleaned_data['content']
            title = f'{name}의 {service} 문의가 등록되었습니다'
            try:
                send_mail(title, content, email, ['tokyo3@netsgo.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact_detail.html", {'form': form})