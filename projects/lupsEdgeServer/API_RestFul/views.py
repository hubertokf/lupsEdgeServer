import django_filters
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from API_RestFul.models import *
from API_RestFul.serializers import *
from django.http import HttpResponse
from django.core import serializers
from rest_framework import filters, generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
import json

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

    @api_view(['GET',])
    def getSchedules(request, *args, **kwargs):
        queryset = Schedule.objects.filter(sensor_id=1)
        serializer_class = ScheduleSerializer
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)

        #posts = (Schedule.objects.filter(sensor_id=1).values('id', 'schType', 'status', 'cron', 'interval', 'date', 'sensor'))
        #json_posts = json.dumps(list(posts))
        return response

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
