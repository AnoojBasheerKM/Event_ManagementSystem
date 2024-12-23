from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    
    phone = models.CharField(max_length=10,unique=True)
    
    
    def __str__(self):
        return self.username
    
class Events(models.Model):
    
    title = models.CharField(max_length=200,null=False)

    description = models.CharField(max_length=200,null=False)
    
    event_date = models.DateField(null=True)
    
    event_time = models.TimeField(null=True)
    
    location = models.CharField(max_length=100)

    created_date = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="events")
    
    def __str__(self):
    
        return self.title

    
    
    