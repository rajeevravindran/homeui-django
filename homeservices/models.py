# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from services import startAlarm
# Create your models here.
import pika
# Create your views here.



class AlarmEvent(models.Model):
    AlarmName = models.CharField(max_length=255,help_text="Name of the Alarm")
    AlarmTime = models.DateTimeField()
    AlarmKilled = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.AlarmName + " : " + str(self.AlarmTime)

    def save(self,*args,**kwargs):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='alarm')
        channel.basic_publish(exchange='',
                              routing_key='alarm',
                              body=startAlarm(self.AlarmTime,"/home/pi/rocky.mp3"))
        super(AlarmEvent,self).save(*args,**kwargs)