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

    def regra(self,id_sensor,valor,id_gateway):   # Verificar argumentos e criar objeto p chamar regras
        engine = EngineRule()

        string_rule = '{{ "evento": "e", "id": "{0}","valor": {1}, "id_gateway": {2} }}'.format(id_sensor,valor,id_gateway)
        #print(string_rule)
        engine.run_rules(string_rule)

        #print('ENTROU NA REGRA')

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

        #print(json['id_sensor'])

        id_g = formation['id_gateway']
        id_s = formation['id_sensor']
        value = formation['value']
        # contador = formation['contador']

        #print("VAL:  "+value)
        #print("ID G: "+ id_g)
        #print("ID S: "+ id_s)

        #print(id_s)
        #return self.get_val_sensor();
        self.regra(id_s,value,id_g)

        #id_sensor, value, contextServer
        #publicacao = Publisher()
        #publicacao.set_publisher_local(json['id_sensor'],value,id_g)
        #publicacao.set_publisher_contexto(value,id_s,id_g)

        #print("REGRA 1")
        #iasdhajkhsdjhad
    def coleting_value_of_sensor(self,parameters_essential_for_colect):

        colecter_sensor = GetValuesSensor()
        formation       = colecter_sensor.get_values_on_gatway(parameters_essential_for_colect)
        return float(formation['value'])            # <--------- Passar argumentos

from core.moduleOfRules.EngineRuleEdge import EngineRule
