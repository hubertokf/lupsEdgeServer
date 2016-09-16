from GetValuesSensor import *
from moduleOfRules.EngineRuleEdge import EngineRule
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

    def regra(self,id_sensor,valor,id_gateway):   # Verificar argumentos e criar objeto p chamar regras
        engine = EngineRule()

        string_rule = '{{ "evento": "e", "id": "{0}","valor": {1}, "id_gateway": {2} }}'.format(id_sensor,valor,id_gateway)
        print(string_rule)
        engine.run_rules(string_rule)

        print('ENTROU NA REGRA')

    def processamento(self,json): # 0 = OBJECT or 1 = FUNCTION
                                # Cria um objeto COMMUNICATION, que retorna um valor do sensor
                                # Realiza um if, verificando se precisa criar um  REGRA ou apenas
                                # retorna um dado
        #valor_sensor =
        colecter_sensor = GetValuesSensor()
        formation = colecter_sensor.get_values_on_gatway(json)            # <--------- Passar argumentos
        #self.set_val_sensor(valor_sensor);
        #print(type(formation))
        #formation = json.loads(formation)

        id_g = formation['id_gateway']
        id_s = formation['id_sensor']
        value = formation['value']
        # contador = formation['contador']

        # print(value)


        #return self.get_val_sensor();
        self.regra(id_s,value,id_g)
        print("REGRA 1")
        #iasdhajkhsdjhad
