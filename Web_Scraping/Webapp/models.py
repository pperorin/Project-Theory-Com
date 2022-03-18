from pyexpat import model
from django.db import models

# Create your models here.

class Mouse(models.Model):
    MouseId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)
    Brand = models.CharField(max_length=500,blank=True)
    PictureLink = models.CharField(max_length=500,blank=True)
    Detail = models.CharField(max_length=500,default="None")
    Banana = models.CharField(max_length=500,default="None")
    PowerB = models.CharField(max_length=500,default="None")
    Jib = models.CharField(max_length=500,default="None")

class Keyboard(models.Model):
    KeyboardId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)
    Brand = models.CharField(max_length=500,blank=True)
    PictureLink = models.CharField(max_length=500,blank=True)
    Detail = models.CharField(max_length=500,default="None")
    Banana = models.CharField(max_length=500,default="None")
    PowerB = models.CharField(max_length=500,default="None")
    Jib = models.CharField(max_length=500,default="None")

class HeadGear(models.Model):
    HeadGearId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)
    Brand = models.CharField(max_length=500,blank=True)
    PictureLink = models.CharField(max_length=500,blank=True)
    Detail = models.CharField(max_length=500,default="None")
    Banana = models.CharField(max_length=500,default="None")
    PowerB = models.CharField(max_length=500,default="None")
    Jib = models.CharField(max_length=500,default="None")