from pyexpat import model
from django.db import models

# Create your models here.

class Mouse(models.Model):
    MouseId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)
    Brand = models.CharField(max_length=500,blank=True)
    PictureLink = models.CharField(max_length=500,blank=True)
    Detail = models.CharField(max_length=20000,default="ไม่มีข้อมูล")
    Banana = models.CharField(max_length=500,default="0")
    Ihavecpu = models.CharField(max_length=500,default="0")

class Keyboard(models.Model):
    KeyboardId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)
    Brand = models.CharField(max_length=500,blank=True)
    PictureLink = models.CharField(max_length=500,blank=True)
    Detail = models.CharField(max_length=20000,default="ไม่มีข้อมูล")
    Banana = models.CharField(max_length=500,default="0")
    Ihavecpu = models.CharField(max_length=500,default="0")

class HeadGear(models.Model):
    HeadGearId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)
    Brand = models.CharField(max_length=500,blank=True)
    PictureLink = models.CharField(max_length=500,blank=True)
    Detail = models.CharField(max_length=500,default="ไม่มีข้อมูล")
    Banana = models.CharField(max_length=500,default="0")
    Ihavecpu = models.CharField(max_length=500,default="0")