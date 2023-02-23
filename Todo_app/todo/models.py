from django.db import models

# Create your models here.


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)        #auto now add used for current date and time

    def __str__(self):   #for storing as a string in database
       return self.title  #for identify this string belongs to which field
#
class login(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)


class register(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.EmailField(max_length=300)


