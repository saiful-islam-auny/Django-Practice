from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from . import models

# Create your views here.
def add_musician(request):
    if request.method=='POST':
         musician_form=forms.musicianForm(request.POST)
         if musician_form.is_valid():
              musician_form.save()
              return redirect('add_musician')
    else:
          musician_form=forms.musicianForm()


   
    return render(request,'add_musician.html',{'form':musician_form})


def edit_musician(request,id):
     musician_data=models.musician.objects.get(pk=id)
     musician_form=forms.musicianForm(instance=musician_data)
     if request.method=='POST':
         musician_form=forms.musicianForm(request.POST,instance=musician_data)
         if musician_form.is_valid():
              musician_form.save()
              return redirect('homepage')
   
     return render(request,'add_musician.html',{'form':musician_form})
