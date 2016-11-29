from core.communication import *
import json

class Proceeding(object):

    core = None

    def __init__(self, parent):             #instância do objeto e inicia o escalonador

        self.core = parent

    def processamento(self, jsonObject):

        acting_actuador = Communication(self.core)

        acting_actuador.set_values_on_gatwat(jsonObject)

        #formation = colecter_sensor.get_values_on_gatway(jsonObject)            #

        # if jsonObject['collect_to_rule']:
        #     return formation
        # else:
        #     self.regra(formation)
        #     return None
