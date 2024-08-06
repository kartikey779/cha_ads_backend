from django.db import models
from django.utils import timezone


# Create your models here
class replies(models.Model):
    customer = models.CharField(max_length=150, blank=True)
    message = models.CharField(max_length=150)
    date = models.DateField()
    
    def __str__(self):
        return self.customer
    
    
class Templates(models.Model):
    template_name = models.CharField(max_length=50)
    template_type = models.CharField(max_length=100)
    template_message = models.CharField(max_length=500)
    status = models.CharField(max_length=50,blank=True)
    date = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.template_name

class Media(models.Model):
    url = models.URLField(blank=True)
    img_id = models.CharField(max_length=1000, primary_key=True)

    def __str__(self):
        return self.img_id


class Contact(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    tags = models.JSONField()

    def __str__(self):
        return self.name
    
    