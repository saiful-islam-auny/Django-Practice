from django.shortcuts import render, redirect
from . import forms 
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.contrib import messages
from Album.models import album
from Musician.models import musician
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')
    
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register_login.html', {'form' : register_form, 'type' : 'Register'})

class UserLoginView(LoginView):
    template_name = 'register_login.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    

@login_required
def profile(request):
  
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('homepage')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'profile.html', {'form' : profile_form})







def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form' : form})


def user_logout(request):
    logout(request)
    return redirect('user_login')