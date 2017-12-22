from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework.authtoken.models import Token
from datetime import date
from django_filters import rest_framework as filters

class Manufacturer(models.Model):
	name = models.CharField(max_length=200)
	website = models.URLField(max_length=200)

	def __str__(self):
		return self.name

class Gateway(models.Model):
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL,null=True)
	uuID = models.CharField(max_length=36,unique=True)
	url = models.URLField(max_length=200,null=True)

	def __str__(self):
		return self.uuID

class GatewayFilter(filters.FilterSet):
    class Meta:
        model = Gateway
        fields = ('uuID', 'manufacturer')

class Actuator(models.Model):
	gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE)
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL,null=True)
	uuID = models.CharField(max_length=36,unique=True)

	def __str__(self):
		return self.uuID

class ActuatorFilter(filters.FilterSet):
    class Meta:
        model = Actuator
        fields = ('uuID', 'gateway', 'manufacturer')

class BaseParameter(models.Model):
	parameter = models.CharField(max_length=200)
	value = models.CharField(max_length=200)

	def __str__(self):
		return self.parameter + ': ' + self.value

class ContextServer(models.Model):
	name = models.CharField(max_length=200)
	addressUrl = models.URLField(max_length=200)
	accessToken = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.name

class SensorType(models.Model):
	name = models.CharField(max_length=200)
	unit = models.CharField(max_length=5)

	def __str__(self):
		return self.name

class Sensor(models.Model):
	gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE)
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL,null=True)
	sensorType = models.ForeignKey(SensorType, on_delete=models.SET_NULL,null=True)
	uuID = models.CharField(max_length=36,unique=True)
	model = models.CharField(max_length=30)

	def __str__(self):
		return self.uuID

class SensorFilter(filters.FilterSet):
    class Meta:
        model = Sensor
        fields = ('uuID', 'gateway', 'sensorType', 'manufacturer')

class Persistance(models.Model):
	sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING)
	contextServer = models.ForeignKey(ContextServer, on_delete=models.PROTECT)
	collectDate = models.DateTimeField(auto_now=False, auto_now_add=False)
	publisher = models.BooleanField(default=False)
	value = models.FloatField()

	def __str__(self):
		return str(self.value)

class PersistanceFilter(filters.FilterSet):
    class Meta:
        model = Persistance
        fields = ('sensor', 'collectDate', 'contextServer', 'publisher')

class Rule(models.Model):
	sensor = models.ForeignKey(Sensor, on_delete=models.SET_NULL,null=True)
	jsonRule = models.TextField()
	status = models.BooleanField()
	topico = models.CharField(max_length=200, default='SOME STRING')
	#topico = models.CharField(max_length=200)

	def __str__(self):
		return self.jsonRule

class RuleFilter(filters.FilterSet):
    class Meta:
        model = Rule
        fields = ('sensor', 'status')

class Schedule(models.Model):
	event_choices = (
		('gathering', 'Gather'),
		('proceeding', 'Act'),
		('publisher', 'Publish'),
	)
	sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
	status = models.BooleanField()
	event = models.CharField(max_length=30, choices=event_choices, null=True)
	# year = models.IntegerField(default=date.today().year,blank=True,validators=[MinValueValidator(date.today().year-40),MaxValueValidator(date.today().year)])
	# month = models.IntegerField(default=1,blank=True,validators=[MinValueValidator(1),MaxValueValidator(12)])
	# day = models.IntegerField(default=1,blank=True,validators=[MinValueValidator(1),MaxValueValidator(31)])
	# hour = models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0),MaxValueValidator(23)])
	# minute = models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0),MaxValueValidator(59)])
	year = models.CharField(max_length=30, null=True)
	month = models.CharField(max_length=30, null=True)
	day = models.CharField(max_length=30, null=True)
	hour = models.CharField(max_length=30, null=True)
	minute = models.CharField(max_length=30, null=True)
	second = models.CharField(max_length=30, null=True)

	def __str__(self):
		return str(self.sensor)

class ScheduleFilter(filters.FilterSet):
    class Meta:
        model = Schedule       
        fields = ('sensor', 'status', 'year', 'month', 'day', 'hour', 'minute', 'second')

class Topicos(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)
