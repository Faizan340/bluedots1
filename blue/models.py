from django.db import models

# Create your models here.
class Form(models.Model):
    fullname = models.CharField(max_length=1000,default="fullname")
    email = models.EmailField(max_length=1000,default="email@gmail.com")
    number = models.IntegerField(default=0000000000)
    address = models.TextField(default="abcd")
    xpercentage = models.IntegerField(default=00)
    xiipercentage = models.IntegerField(default=00)
    training = models.CharField(max_length=1000,default="training")
    city = models.CharField(max_length=1000,default="city")
    def __str__(self):
        return self.fullname