from django.db import models


# Create your models here
class replies(models.Model):
    customer = models.CharField(max_length=150, blank=True)
    message = models.CharField(max_length=150)
    date = models.DateField()
    
    def __str__(self):
        return self.customer
    
    
class Templates(models.Model):
    template_name = models.CharField(max_length=50)
    templates = models.CharField(max_length=500)
    
    def __str__(self):
        return self.template_name
    
    
    