from django.shortcuts import render
# from Musician.models import musician
from Album.models import album

def home(request):
    data=album.objects.all()
    return render(request,'home.html',{'data':data})


