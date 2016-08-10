from django.contrib import admin
from .models import *


class ManufacturerAdmin(admin.ModelAdmin):
	list_display = ('name', 'website')
class GatewayAdmin(admin.ModelAdmin):
	list_display = ('manufacturer', 'uuID')
class ActuatorAdmin(admin.ModelAdmin):
	list_display = ('gateway', 'uuID')
class BaseParameterAdmin(admin.ModelAdmin):
	list_display = ('parameter', 'value')
class ContextServerAdmin(admin.ModelAdmin):
	list_display = ('name', 'addressUrl')
class SensorTypeAdmin(admin.ModelAdmin):
	list_display = ('name', 'unit')
class SensorAdmin(admin.ModelAdmin):
	list_display = ('gateway', 'manufacturer', 'sensorType', 'uuID', 'model')
class PersistanceAdmin(admin.ModelAdmin):
	list_display = ('sensor', 'contextServer', 'collectDate', 'value')
class RuleAdmin(admin.ModelAdmin):
	list_display = ('sensor', 'jsonRule', 'status')
class ScheduleAdmin(admin.ModelAdmin):
	list_display = ('sensor', 'status', 'year', 'month', 'day', 'hour', 'minute')

admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Gateway, GatewayAdmin)
admin.site.register(Actuator, ActuatorAdmin)
admin.site.register(BaseParameter, BaseParameterAdmin)
admin.site.register(ContextServer, ContextServerAdmin)
admin.site.register(SensorType, SensorTypeAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Persistance, PersistanceAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register(Schedule, ScheduleAdmin)



# Register your models here.
