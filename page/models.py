from django.db import models

# Create your models here.

class yer(models.Model):
    yerVeri = models.CharField(max_length=500,null=False)
    neredeVeri = models.CharField(max_length=500,null=False)