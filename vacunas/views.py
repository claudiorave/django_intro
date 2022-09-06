from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import serializers, status, viewsets, mixins
from .serializers import VacunaSerializer
from .models import Vacuna

def index(request):
    template = loader.get_template('vacunas/index.html')
    vacunas_list = Vacuna.objects.order_by('nombre')
    context = {
        'vacunas_list': vacunas_list,
    }
    return HttpResponse(template.render(context, request))

class VacunaCreateView(CreateView):
    model = Vacuna
    fields = ['nombre', 'fabricante', 'tipo', 'cant_dosis']
    success_url = reverse_lazy('index')

class DetailView(generic.DetailView):
    model = Vacuna
    template_name = 'vacunas/modificar.html'

class VacunaUpdateView(UpdateView):
    model = Vacuna
    fields = ['nombre', 'fabricante', 'tipo', 'cant_dosis']
    success_url = reverse_lazy('index')

class VacunaViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = VacunaSerializer
    queryset = Vacuna.objects.all()

def delete(request, pk):
    Vacuna.objects.filter(pk=pk).delete()
    return redirect("index")
