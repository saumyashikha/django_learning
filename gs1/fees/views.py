from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fee_django(request):
    return HttpResponse('300')

def home_page(request):
    return HttpResponse('Home Page')