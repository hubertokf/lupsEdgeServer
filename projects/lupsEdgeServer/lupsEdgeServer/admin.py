from django.contrib import admin
from .models import *

admin.site.register(Manufacturer)
admin.site.register(Gateway)
admin.site.register(Actuator)
admin.site.register(BaseParameter)
admin.site.register(ContextServer)
admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(Persistance)
admin.site.register(Rule)
admin.site.register(Schedule)


# Register your models here.
