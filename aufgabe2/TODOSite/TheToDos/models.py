from django.db import models
#signal = nachdem etwas in der datenbank gesaved wurde wird ein code ausgefuhrt
#from django.db.models.signal import post_save
##from django.shortcuts import redirect


# Create your models here.
#inherits all the functions from model
class ToDoData(models.Model):
    description = models.CharField(max_length=280, default= '')
    deadline = models.CharField(max_length=24, default= '')
    percent = models.IntegerField(default= '0')

##muss vllt geandert werden    
##def redirect_to_ubersicht(sender, **kwargs):
##   if kwargs['created']:
##        return redirect('/ubersicht.html')

#post_save.connect(redirect_to_ubersicht, sender=ToDoData)