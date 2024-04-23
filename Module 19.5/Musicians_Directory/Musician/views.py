from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from . import models
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView


# Create your views here.



@method_decorator(login_required, name='dispatch')
class AddMusicianCreateView(CreateView):
    model = models.musician
    form_class = forms.musicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')
    def form_valid(self, form):
        form.instance.musician = self.request.user
        return super().form_valid(form)
    



@method_decorator(login_required, name='dispatch')
class EditmusicianView(UpdateView):
    model = models.musician
    form_class = forms.musicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    