from django.core import paginator
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import  login_required
from django.urls import  reverse_lazy
from django.core.paginator import Paginator
from .forms import EquipmentForm
from . import models
from django.db.models import Q
from equipmentMaintenance.models import MaintenanceDB
from .filters import EquipmentFilter, EquipmentMaintenanceFilter
from django import forms

# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa

class MyPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise

class EquipmentListView(ListView):
    template_name = 'equipmentList/equipment_page.html'
    queryset = models.EQUIPMENT_DB.objects.all()
    # paginate_by = 50
    # paginator_class = MyPaginator
    # paginator = Paginator(queryset, per_page=50)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EquipmentFilter(self.request.GET, queryset=self.queryset)
        return context

    # Getting the equipment vs maintenance views and filtering them
class EquipmentMaintenanceListView(ListView):
    template_name = 'equipmentList/equipment_maintenance_detail.html'
    queryset = MaintenanceDB.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EquipmentMaintenanceFilter(self.request.GET, queryset=self.queryset)
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
