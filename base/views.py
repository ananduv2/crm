from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy


from .models import Activity
# Create your views here.


#Class to list all activities
class ActivityList(ListView):
    model = Activity
    context_object_name = 'activities'


#Class to update an activity
class ActivityUpdate(UpdateView):
    model = Activity
    fields = '__all__'
    success_url = reverse_lazy('activities')
    template_name = 'base/edit.html'

#Class to create new activity
class ActivityCreate(CreateView):
    model = Activity
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('activities')
    template_name = 'base/create.html'
    


