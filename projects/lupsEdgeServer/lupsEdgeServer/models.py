from django.db import models

class Actuators(models.Model):
	gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE)
	uuID = models.CharField(max_length=36)

class BaseParameters(models.Model):
	parameter = models.CharField(max_length=200)
	value = models.CharField(max_length=200)

class ContextServers(models.Model):
	name = models.CharField(max_length=200)
	addressUrl = models.URLField(max_length=200)

class Gateways(models.Model):
	manufacturer = models.ForeignKey(Manufacturers, on_delete=models.SET_NULL)
	uuID = models.CharField(max_length=36)

class Manufacturers(models.Model):
	name = models.CharField(max_length=200)
	website = models.URLField(max_length=200)

class Persistances(models.Model):
	sensor = models.ForeignKey(Sensors, on_delete=models.PROTECT)
	contextServer = models.ForeignKey(ContextServers, on_delete=models.PROTECT)
	collectDate = models.DateTimeField(auto_now=False, auto_now_add=False)
	value = models.FloatField()

class Rules(models.Model):
	sensor = models.ForeignKey(Sensors, on_delete=models.SET_NULL)
	jsonRule = models.CharField(max_length=None)
	status = models.BooleanField()

class Schedules(models.Model):
	schedules_choices = (
        ('i', 'Interval'),
        ('d', 'Date'),
        ('c', 'Cron'),
    )
	sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE)
	schType = models.CharField(max_length=1, choices=schedules_choices, default='i')
	status = models.BooleanField()
	cron = models.CharField(max_length=None)
	interval = models.CharField(max_length=None)
	date = models.CharField(max_length=None)

class Sensors(models.Model):
	gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE)
	manufacturer = models.ForeignKey(Manufacturers, on_delete=models.SET_NULL)
	sensorType = models.ForeignKey(SensorsTypes, on_delete=models.SET_NULL)
	uuID = models.CharField(max_length=36)
	model = models.CharField(max_length=30)

class SensorsTypes(models.Model):
	name = models.CharField(max_length=200)
	unit = models.CharField(max_length=5)
