from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def learn_django(request):
    cname = 'Django'
    duration = '30 months'
    seats = 10
    django_details = {'nm':cname, 'du':duration, 's':seats}
    return render(request, 'courses/courses.html', django_details)

def learn_python(request):
    return HttpResponse('<h1>hello python</h1>')

def learn_var(request):
    a = '<h1>Hello varible</h1>'
    return HttpResponse(a)

def learn_format(request):
    a = 's'
    return HttpResponse(f'Hello how are u {a}')
    
        