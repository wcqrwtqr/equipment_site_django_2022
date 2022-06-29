from django.views.generic import TemplateView,ListView, DetailView, View, CreateView, DeleteView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import  login_required
from django.urls import  reverse_lazy

from .forms import EquipmentForm
from . import models
from .filters import EquipmentFilter
from django import forms
# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
# from xhtml2pdf import pisa



class EquipmentListView(ListView):
    template_name = 'equipmentList/equipment_page.html'
    context_object_name = 'equipment_1'
    queryset = models.EQUIPMENT_DB.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EquipmentFilter(self.request.GET, queryset=self.queryset)
        return context



class EquipmentDetailView(DetailView):
    template_name = 'equipmentList/equipment_detail.html'
    queryset = models.EQUIPMENT_DB.objects.all()
    context_object_name = 'equipment_detail'


class EquipmentCreateView(CreateView):
    template_name = 'equipmentList/equipment_new.html'
    form_class = EquipmentForm
    model = models.EQUIPMENT_DB
    success_url = reverse_lazy('equipment')

    def from_valid(self,form):
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)

class EquipmentDeleteView(DeleteView):
    model = models.EQUIPMENT_DB
    success_url = reverse_lazy('equipment')
    template_name = 'equipmentList/equipment_confirm_delete.html'

class EquipmentUpdateView(UpdateView):
    model = models.EQUIPMENT_DB
    fields = '__all__'
    template_name = 'equipmentList/equipment_update.html'
    success_url = reverse_lazy('equipment')
