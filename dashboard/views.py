from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def add_property(request):
    return HttpResponse('add_property_list')

def view_property(request):
    return HttpResponse('view_property')    
