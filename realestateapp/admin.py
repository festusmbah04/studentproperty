from django.contrib import admin
from realestateapp.models import *
# Register your models here.

admin.site.register(Location)
admin.site.register(propertyType)

@admin.register(Property)
class propertyAdmin(admin.ModelAdmin):
    
    pass

admin.site.register(ContactAgent)

