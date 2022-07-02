from operator import truediv
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#class account(models.Model):    
#    name=models.CharField(unique=True, max_length=30)
#    mail=models.EmailField(unique=True)
#    pass5=models.CharField(max_length=30)

class solofftournament(models.Model):
    tittle=models.CharField(max_length=30)
    totalplayer=models.CharField(max_length=10)
    time=models.CharField(max_length=30)
    prize=models.CharField(max_length=30)

class duofftournament(models.Model):
    tittle=models.CharField(max_length=30)
    totalplayer=models.CharField(max_length=10)
    time=models.CharField(max_length=30)
    prize=models.CharField(max_length=30)

class squadfftournament(models.Model):
    tittle=models.CharField(max_length=30)    
    totalplayer=models.CharField(max_length=10)
    time=models.CharField(max_length=30)    
    prize=models.CharField(max_length=30)


class freefiredata(models.Model):
    #user=models.ForeignKey(User, on_delete=models.CASCADE ,primary_key=True)
    ffname=models.CharField(max_length=30)
    ffid=models.CharField(max_length=30)

class pubggdata(models.Model):
    #user=models.OneToOneField(User, on_delete=models.CASCADE ,primary_key=True)
    pubgname=models.CharField(max_length=30)
    pubgid=models.CharField(max_length=30)

class coddata(models.Model):
    #user=models.OneToOneField(User, on_delete=models.CASCADE ,primary_key=True)
    codname=models.CharField(max_length=30)
    codid=models.CharField(max_length=30)


