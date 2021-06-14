from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy


from .models import Activity
# Create your views here.
class ActivityList(ListView):
    model = Activity
    context_object_name = 'activities'


