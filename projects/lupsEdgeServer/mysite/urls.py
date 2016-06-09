"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from lupsEdgeServer.views import *
from rest_framework.authtoken import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'gateways', GatewayViewSet)
router.register(r'actuators', ActuatorViewSet)
router.register(r'baseParameters', BaseParameterViewSet)
router.register(r'contextServers', ContextServerViewSet)
router.register(r'sensorsTypes', SensorTypeViewSet)
router.register(r'sensors', SensorViewSet)
router.register(r'persistances', PersistanceViewSet)
router.register(r'rules', RuleViewSet)
router.register(r'schedules', ScheduleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #To obtain auth token (API key) passing User and Password by POST
    url(r'^api-token-auth/', views.obtain_auth_token)
]
