from core.GetValuesSensor import *
# from core.publisher import *
import json

class Gathering(object):

    def set_id(self, id_sensor):
        self.id_sensor = id_sensor

    def get_id(self):
        return self.id_sensor

    def set_val_sensor(self, vsensor):
        self.vsensor = vsensor

    def get_val_sensor(self):
        return self.vsensor

    def regra(self,json_result_gathering):   # Verificar argumentos e criar objeto p chamar regras
        engine = EngineRule()

        string_rule = '{{ "evento": "e", "id": "{0}","valor": {1}, "id_gateway": {2} }}'.format(json_result_gathering['id_sensor'],json_result_gathering['value'],json_result_gathering['id_gateway'],json_result_gathering['collectDate'])
        #print(string_rule)
        engine.run_rules(string_rule)

        #print('ENTROU NA REGRA')

    def processamento(self,json): # 0 = OBJECT or 1 = FUNCTION
                                # Cria um objeto COMMUNICATION, que retorna um valor do sensor
                                # Realiza um if, verificando se precisa criar um  REGRA ou apenas
                                # retorna um dado

        colecter_sensor = GetValuesSensor()
        formation = colecter_sensor.get_values_on_gatway(json)            #
        self.regra(formation)

    def processamento1(self,json): # 0 = OBJECT or 1 = FUNCTION
                                # Cria um objeto COMMUNICATION, que retorna um valor do sensor
                                # Realiza um if, verificando se precisa criar um  REGRA ou apenas
                                # retorna um dado

        colecter_sensor = GetValuesSensor()
        formation = colecter_sensor.get_values_on_gatway(json)            #
        #self.regra(formation)
        return formation


    def coleting_value_of_sensor(self,parameters_essential_for_colect):

        colecter_sensor = GetValuesSensor()
        formation       = colecter_sensor.get_values_on_gatway(parameters_essential_for_colect)
        return formation            # <--------- Passar argumentos

from core.moduleOfRules.EngineRuleEdge import EngineRule
