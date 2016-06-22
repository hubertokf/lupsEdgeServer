import django_filters
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from API_RestFul.models import *
from API_RestFul.serializers import *
from rest_framework import filters
from rest_framework import generics

# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufactureSerializer

class GatewayViewSet(viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['uuID', 'manufacturer']

class ActuatorViewSet(viewsets.ModelViewSet):
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['uuID', 'gateway', 'manufacturer']

class BaseParameterViewSet(viewsets.ModelViewSet):
    queryset = BaseParameter.objects.all()
    serializer_class = BaseParameterSerializer

class ContextServerViewSet(viewsets.ModelViewSet):
    queryset = ContextServer.objects.all()
    serializer_class = ContextServerSerializer

class SensorTypeViewSet(viewsets.ModelViewSet):
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['uuID', 'gateway', 'sensorType', 'manufacturer']

class PersistanceViewSet(viewsets.ModelViewSet):
    queryset = Persistance.objects.all()
    serializer_class = PersistanceSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['sensor', 'collectDate', 'contextServer']

class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['sensor', 'status']

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['schType', 'sensor', 'status']
