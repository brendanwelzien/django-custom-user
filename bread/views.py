from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Bread
from django.urls import reverse_lazy

class BreadListView(ListView): # template and model
    template_name = "bread/bread-list.html"
    model = Bread

class BreadDetailView(DetailView):
    template_name = "bread/bread-detail.html"
    model = Bread

class BreadUpdateView(UpdateView):
    template_name = "bread/bread-update.html"
    model = Bread
    fields = ['name', 'description']

class BreadDeleteView(DeleteView):
    template_name = "bread/bread-delete.html"
    model = Bread
    sucess_url = reverse_lazy('bread-list')

class BreadCreateView(CreateView):
    template_name = "bread/bread-create.html"
    model = Bread
    fields = ['name', 'description']