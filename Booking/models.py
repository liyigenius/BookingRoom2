from django.db import models
from django.contrib.auth.models import User
from registration.models import *


class Room(models.Model):
    name = models.CharField(max_length = 50)
    addr = models.CharField(max_length = 50)
    owner = models.ForeignKey(RegistrationProfile)
    
    desc = models.CharField(max_length = 500)
    

class Order (models.Model):
    user = models.ForeignKey(RegistrationProfile)
    room = models.ForeignKey(Room)
    status = models.IntegerField()
    dt = models.DateTimeField()
    
class TimeSlot(models.Model):
    yr = models.IntegerField()
    mt = models.IntegerField()
    dt = models.IntegerField()
    seg1 = models.IntegerField()
    seg2 = models.IntegerField()
    
class RoomStatus(models.Model):
    room = models.ForeignKey(Room)
    ts = models.ForeignKey(TimeSlot)     
    
    
       
    