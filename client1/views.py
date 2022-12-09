from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from django.db import models

from .forms import CreatePersoneForm 
from .models import Persone, Phone

class HomePageView(TemplateView):
    template_name='../templates/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_by = self.request.GET.get('search_by')
        query = self.request.GET.get('query')
        search_message = 'All customers'
        if search_by in ['phone', 'second_name'] and search_by:
            if search_by == 'second_name':
                persons = Persone.objects.filter(second_name=query)
                search_message = f'Searching for "second_name" by "{query}"'
            else:
                persons = Persone.objects.filter(phones__phone=query)
                search_message = f'Searching for "phones" by "{query}"'
        else:
            persons = Persone.objects.all()
        context["persons"] = persons
        context["search_message"] = search_message
        return context
    

class AddNewFormView(CreateView):
    template_name="../templates/add_persone.html"
    form_class = CreatePersoneForm
    success_url = reverse_lazy('home')
    def get_success_url(self):
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            Phone.objects.create(phone=phone_number, contact=self.object)
        return super().get_success_url()
    
class EditFormView(UpdateView):
    template_name="../templates/edit_persone.html"
    form_class = CreatePersoneForm
    model = Persone
    success_url = reverse_lazy('home')
    def get_success_url(self):
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            Phone.objects.create(phone=phone_number, contact=self.object)
        return super().get_success_url()

class DeletePersonView(DeleteView):
    model = Persone
    template_name="../templates/delete_persone.html"
    success_url = reverse_lazy('home') 
    
