from django.shortcuts import render, redirect
from . form import ExampleForm, StudentForm
from . import models

def home(request):
    return render(request, 'home.html')

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ExampleForm()
    return render(request, 'djangoform.html', {'form': form})



def home(request):
    student = models.Student.objects.all()
    return render(request,"home.html", {'data': student})

def delete_student(request, roll):
    std = models.Student.objects.get(pk = roll).delete()
    return redirect("home")


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form' : form})