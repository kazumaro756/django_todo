from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,DeleteView,UpdateView
from .models import todomodel
from django.urls import reverse_lazy
# Create your views here.

class Todolist(ListView):
    template_name = 'list.html'
    model = todomodel

class Tododetail(DetailView):
    template_name = 'detail.html'
    model = todomodel

class Todocreate(CreateView):
    template_name = 'create.html'
    model = todomodel
    fields = ('title','memo','priority','duedate')
    success_url = reverse_lazy('list')

class Tododelete(DeleteView):
    template_name = 'delete.html'
    model = todomodel
    success_url = reverse_lazy('list')

class Todoupdate(UpdateView):
    template_name = 'update.html'
    model = todomodel
    success_url = reverse_lazy('list')
    fields = ('title','memo','priority','duedate')