from django.db import models

# Create your models here.

class Mouse(models.Model):
    MouseId = models.AutoField(primary_key=True)
    MouseName = models.CharField(max_length=500)

class Keyboard(models.Model):
    KeyboardId = models.AutoField(primary_key=True)
    KeyboardName = models.CharField(max_length=500)