from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models import *
import json
import requests

@receiver(post_save, sender=Schedule)
def post_save_sched(sender, instance, created, **kwargs):
    data =  {"id": str(instance.id), "event": str(instance.event),"status": str(instance.status),"year": str(instance.year),"month": str(instance.month),"day": str(instance.day),"hour": str(instance.hour),"minute": str(instance.minute), "second": str(instance.second),"sensor": str(instance.sensor.id),"signal":"saved"}
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://localhost:8081/sigSchedule_add', data=json.dumps(data), headers=headers)


@receiver(post_delete, sender=Schedule)
def post_delete_sched(sender, instance, **kwargs):
    data =  {"id": str(instance.id),"status": str(instance.status),"year": str(instance.year),"month": str(instance.month),"day": str(instance.day),"hour": str(instance.hour),"minute": str(instance.minute),"sensor": str(instance.sensor.id),"signal":"deleted"}
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://localhost:8081/sigSchedule_delete', data=json.dumps(data), headers=headers)

@receiver(post_save, sender=Sensor)
def post_save_sensor(sender, instance, created, **kwargs):
    data =  {"id": str(instance.id),"uuID": str(instance.uuID),"model": str(instance.model),"gateway": str(instance.gateway.id),"manufacturer": str(instance.manufacturer),"sensorType": str(instance.sensorType),"signal":"saved"}
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://localhost:8081/sigSensor_add', data=json.dumps(data), headers=headers)

@receiver(post_delete, sender=Sensor)
def post_delete_sensor(sender, instance, **kwargs):
    data =  {"id": str(instance.id),"uuID": str(instance.uuID),"model": str(instance.model),"gateway": str(instance.gateway.id),"manufacturer": str(instance.manufacturer),"sensorType": str(instance.sensorType),"signal":"deleted"}
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://localhost:8081/sigSensor_delete', data=json.dumps(data), headers=headers)
