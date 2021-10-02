from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
class Clientrequest(models.Model):
    name= models.CharField(max_length=30)
    email= models.EmailField(max_length=50)
    phone= models.CharField(max_length=15)
    SERVICE = (('Web design and development', 'Web design and development'), ('Android application development', 'Android application development'), ('Desktop application development', 'Desktop application development'),('CCTV installation/Network solutions', 'CCTV installation/Network solutions'),('Computer repair and maintenance', 'Computer repair and maintenance'),)
    service = models.CharField(max_length=50, choices=SERVICE, null=True)
    STATE = (('Kenya', 'Kenya'), ('Uganda', 'Uganda'), ('Tanzania', 'Tanzania'),('Ethiopia', 'Ethiopia'),('Sudan', 'Sudan'),('Somalia', 'Somalia'),('South Sudan', 'South Sudan'),('Rwanda', 'Rwanda'),('Burundi', 'Burundi'),('Djibouti', 'Djibouti'))
    country = models.CharField(max_length=15, choices=STATE,null=True)
    HOW = (('Social media', 'Social media'), ('Friends/Colleague', 'Friends/Colleague'), ('Web search', 'Web search'),)
    how = models.CharField(max_length=20, choices=HOW,null=True)
    message=models.TextField(max_length=300,null=True)
    date= models.DateTimeField(default=timezone.now())
    
    class Meta:
        ordering = ["-pk"]

    

