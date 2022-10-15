
from django.core.checks import messages
from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.

RENT = 'rent'
SALE = 'sale'
CHOOSE = ''
OFFER_TYPE = [ 
    (RENT, 'rent'),
    (SALE, 'sale'),
    (CHOOSE, 'choose offer_type'),
]

class propertyType(models.Model):
    property_type_name = models.CharField(max_length=50, unique=True)

    class Meta():
        verbose_name_plural = 'My Property Type'

    def __str__(self):
        return self.property_type_name

    def save(self, *args, **kwargs):
        self.property_type_name = self.property_type_name.capitalize()
        return super().save(*args, **kwargs)

class  Location(models.Model):
    location_name = models.CharField(max_length=50, unique=True)

    class Meta():
        verbose_name_plural = 'Location'

    def __str__(self):
        return self.location_name

    def save(self, *args, **kwargs):
        self.location_name = self.location_name.capitalize()
        return super().save(*args, **kwargs)



    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    property_type = models.ForeignKey(propertyType, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    prop_img1 = models.ImageField( verbose_name ='property Image 1', null=True, blank=True, upload_to='uploads/')
    prop_img2 = models.ImageField( verbose_name ='property Image 2',null=True, blank=True, upload_to='uploads/')
    prop_img3 = models.ImageField( verbose_name ='property Image 3',null=True, blank=True, upload_to='uploads/')
    offer_type =models.CharField(max_length=15, choices=OFFER_TYPE, default=CHOOSE)
    description = models.TextField()
    address = models.TextField()
    numbers = models.PositiveBigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    
class Property(models.Model):
    property_name = models.CharField(max_length=200)

    def __str__(self):
        return self.property_name

    class Meta():
        verbose_name_plural ='property'    
    
    def save(self, *args, **kwargs):
        self.property_name = self.property_name.capitalize()
        return super().save(*args, **kwargs)    

    def get_absolute_url(self):
        return reversed('realesateapp:property_datail', kwargs={'slug':self.slug})
  

class ContactAgent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE,null=True, blank=True)
    message = models.TextField()
