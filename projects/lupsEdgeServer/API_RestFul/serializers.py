from rest_framework import serializers
from django.contrib.auth.models import User, Group

from API_RestFul.models import *

# Serializers define the API representation.
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'groups')

class ManufactureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class GatewaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gateway
        fields = '__all__'

class ActuatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actuator
        fields = '__all__'

class BaseParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseParameter
        fields = '__all__'

class ContextServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContextServer
        fields = '__all__'

class SensorTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorType
        fields = '__all__'

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class PersistanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persistance
        fields = '__all__'

class RuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

