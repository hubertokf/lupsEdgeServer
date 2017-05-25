from rest_framework import serializers
from django.contrib.auth.models import User, Group

from API_RestFul.models import *

# Serializers define the API representation.
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'groups')

class ManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = '__all__'

class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = '__all__'

class BaseParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseParameter
        fields = '__all__'

class ContextServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContextServer
        fields = '__all__'

class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class PersistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persistance
        fields = '__all__'

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class TopicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topicos
        fields = '__all__'
