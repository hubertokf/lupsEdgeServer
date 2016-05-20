from django.contrib import admin
from .models import *

admin.site.register(Manufacturers)
admin.site.register(Gateways)
admin.site.register(Actuators)
admin.site.register(BaseParameters)
admin.site.register(ContextServers)
admin.site.register(SensorsTypes)
admin.site.register(Sensors)
admin.site.register(Persistances)
admin.site.register(Rules)
admin.site.register(Schedules)


# Register your models here.
