from django.urls import path, include
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.view_property, name='view_property'),
    path('add_property/', views.view_property, name='add_property'),
]