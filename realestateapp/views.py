from django.shortcuts import render
from django.http import HttpResponse
from realestateapp.models import *
# Create your views here.

# def home(request):
#     return HttpResponse('Home Page')

# def about(request):
#     return HttpResponse('about us') 

# def contact(request):
#     return HttpResponse('contact')

# def property_list(request):
#     return HttpResponse('property_list')    

def home(request):
    rent = property.object.filter(offer_type='Rent').order_by('-created')[:3]
    sale = property.object.filter(offer_type='Rent').order_by('-created')[:3]
    home_data = {
        'rent':rent,
        'sal':sale
    }
    return render(request, 'realestateapp/index.html',home_data)

def home(request):
    return render(request,'realestateapp/index.html')

def about(request):
    return render(request,'realestateapp/about.html')

def property_rent(request):
    rent = property.objects.filter(offer_type='Rent')
    return render(request, 'realestateapp/rent.html', {'rent':rent})

def property_listing(request):
    return render(request, 'realestateapp/property_list')
    
def property_details(request, slug):
    datail = property.object.get(slug=slug)
    return render(request, 'realestateapp')    

def get_property_from_type(request, prop_id):
    get_prop = property.objects.filter(property_type_id=prop_id)
        


def product(request):
    return render(request,'product')

def request(request):
    return render(request,'request')    


