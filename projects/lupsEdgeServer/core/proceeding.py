from core.communication import *
import json

class Proceeding(object):

    request_API_to_DB = None

    def __init__(self, request_API):
        self.request_API_to_DB = request_API

    def processamento(self, jsonObject):

        acting_actuador = Communication(self.request_API_to_DB)

        acting_actuador.set_values_on_gatwat(jsonObject)

        #formation = colecter_sensor.get_values_on_gatway(jsonObject)            #

        # if jsonObject['collect_to_rule']:
        #     return formation
        # else:
        #     self.regra(formation)
        #     return None
