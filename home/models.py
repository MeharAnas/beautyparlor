from django.db import models

# Create your models here.
    
class Booking(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Number = models.CharField(max_length=20)
    Category = models.CharField(max_length=200)
    Date = models.DateTimeField()
    Message = models.TextField(max_length=500)