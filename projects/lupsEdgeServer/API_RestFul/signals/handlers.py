from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models import *
import json
import requests

@receiver(post_save, sender=Schedule)
def post_save_sched(sender, instance, created, **kwargs):
    data =  {"id": instance,"status": instance.status,"year": instance.year,"month": instance.month,"day": instance.day,"hour": instance.hour,"minute": instance.minute,"sensor": instance.sensor}
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://localhost:8081/sigSchedule', data=json.dumps(data), headers=headers)


@receiver(post_delete, sender=Schedule)
def post_delete_sched(sender, instance, **kwargs):
    data =  {"id": instance,"status": instance.status,"year": instance.year,"month": instance.month,"day": instance.day,"hour": instance.hour,"minute": instance.minute,"sensor": instance.sensor}
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://localhost:8081/sigSchedule', data=json.dumps(data), headers=headers)

@receiver(post_save, sender=Sensor)
def post_save_sensor(sender, instance, created, **kwargs):
    data =  {"id": instance,"uuID": instance.uuID,"model": instance.model,"gateway": instance.gateway,"manufacturer": instance.manufacturer,"sensorType": instance.sensorType}
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://localhost:8081/sigSensor', data=json.dumps(data), headers=headers)

@receiver(post_delete, sender=Sensor)
def post_delete_sensor(sender, instance, **kwargs):
    data =  {"id": instance,"uuID": instance.uuID,"model": instance.model,"gateway": instance.gateway,"manufacturer": instance.manufacturer,"sensorType": instance.sensorType}
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://localhost:8081/sigSensor', data=json.dumps(data), headers=headers)