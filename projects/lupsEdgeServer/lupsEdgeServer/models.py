from django.db import models

class Manufacturer(models.Model):
	name = models.CharField(max_length=200)
	website = models.URLField(max_length=200)

class Gateway(models.Model):
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL,null=True)
	uuID = models.CharField(max_length=36)

class Actuator(models.Model):
	gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE)
	uuID = models.CharField(max_length=36)

class BaseParameter(models.Model):
	parameter = models.CharField(max_length=200)
	value = models.CharField(max_length=200)

class ContextServer(models.Model):
	name = models.CharField(max_length=200)
	addressUrl = models.URLField(max_length=200)

class SensorType(models.Model):
	name = models.CharField(max_length=200)
	unit = models.CharField(max_length=5)

class Sensor(models.Model):
	gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE)
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL,null=True)
	sensorType = models.ForeignKey(SensorType, on_delete=models.SET_NULL,null=True)
	uuID = models.CharField(max_length=36)
	model = models.CharField(max_length=30)

class Persistance(models.Model):
	sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT)
	contextServer = models.ForeignKey(ContextServer, on_delete=models.PROTECT)
	collectDate = models.DateTimeField(auto_now=False, auto_now_add=False)
	value = models.FloatField()

class Rule(models.Model):
	sensor = models.ForeignKey(Sensor, on_delete=models.SET_NULL,null=True)
	jsonRule = models.TextField()
	status = models.BooleanField()

class Schedule(models.Model):
	schedules_choices = (
        ('i', 'Interval'),
        ('d', 'Date'),
        ('c', 'Cron'),
    )
	sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
	schType = models.CharField(max_length=1, choices=schedules_choices, default='i')
	status = models.BooleanField()
	cron = models.TextField()
	interval = models.TextField()
	date = models.TextField()

