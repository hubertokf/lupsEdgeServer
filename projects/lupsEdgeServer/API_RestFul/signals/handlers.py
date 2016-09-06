from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models import *
import requests

@receiver(post_save, sender=Schedule)
def post_save_sched(sender, instance, created, **kwargs):
	r = requests.get('http://localhost:8081/sigSchedule')

@receiver(post_delete, sender=Schedule)
def post_delete_sched(sender, instance, **kwargs):
	r = requests.get('http://localhost:8081/sigSchedule')

@receiver(post_save, sender=Sensor)
def post_save_sensor(sender, instance, created, **kwargs):
	r = requests.get('http://localhost:8081/sigSensor')

@receiver(post_delete, sender=Sensor)
def post_delete_sensor(sender, instance, **kwargs):
	r = requests.get('http://localhost:8081/sigSensor')