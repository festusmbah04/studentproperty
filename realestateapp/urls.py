from django.urls import path
from realestateapp import views

app_name = 'realestateapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('property-listing/', views.property_listing, name='property_listing'),
    path('property-rent/', views.property_rent, name='property_rent'),
    path('property-datails/<slug:slug>/', views.property_details, name='property_datails'),
    path('product/',views.product, name='product'),
    path('request/',views.request, name='request'),
    
]