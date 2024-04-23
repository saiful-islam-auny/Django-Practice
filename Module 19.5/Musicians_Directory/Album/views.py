from django.shortcuts import render,redirect
from . import forms
from . import models
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView


# Create your views here

@method_decorator(login_required, name='dispatch')
class AddAlbumCreateView(CreateView):
    model = models.album
    form_class = forms.albumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = models.album
    form_class = forms.albumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    




@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = models.album
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'



