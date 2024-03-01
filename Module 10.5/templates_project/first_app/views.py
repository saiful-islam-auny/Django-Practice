from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timesince import timesince
import datetime


def home(request):
    d = {'name': 'saiful islam auny', 'age': 24, 'location': "Khulna", "cur_time": datetime.datetime.now(), 'inter': 235467, "empty": '', 'courses': [
        {'name': 'Python', 'code': 'PY'},
        {'name': 'Django', 'code': 'DJ'},
        {'name': 'HTML', 'code': 'HT'},
        {'name': 'CSS', 'code': 'CS'},
    ], 
    'line': '''one
            two
            three''',
            'comment': 'I love programming, programming is just about solving problems',
        }
    return render(request, 'home.html', d)
