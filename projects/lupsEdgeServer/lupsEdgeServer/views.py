from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from lupsEdgeServer.models import *
from lupsEdgeServer.serializers import *

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

class ActuatorViewSet(viewsets.ModelViewSet):
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer

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

class PersistanceViewSet(viewsets.ModelViewSet):
    queryset = Persistance.objects.all()
    serializer_class = PersistanceSerializer

class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
