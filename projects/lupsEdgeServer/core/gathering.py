from core.GetValuesSensor import *
# from core.publisher import *
import json

class Gathering(object):

    core = None

    def __init__(self, parent):             #instância do objeto e inicia o escalonador

        self.core = parent

    def regra(self,json_result_gathering):   # Verificar argumentos e criar objeto p chamar regras
        engine = EngineRule(self.core)

        string_rule = '{{ "evento": "e", "id": "{0}","valor": {1}, "id_gateway": {2} }}'.format(json_result_gathering['id_sensor'],json_result_gathering['value'],json_result_gathering['id_gateway'],json_result_gathering['collectDate'])
        #print(string_rule)
        print("chegou no gathering, vai chamar regra")
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



from core.moduleOfRules.EngineRuleEdge import EngineRule
