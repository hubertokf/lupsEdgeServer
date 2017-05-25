# -*- coding: utf-8 -*-
# Em teste
try:
    from business_rules import run_all
    from business_rules.actions import BaseActions, rule_action
    from business_rules.fields import FIELD_NUMERIC, FIELD_TEXT
    from core.moduleOfRules.ActionRules import ActionRules
    from core.moduleOfRules.ConditionsRules import ConditionsRules
    from core.moduleOfRules.Parameters import Parameters
    import requests
    import datetime
    import json
    import os
    import core.event_treatment as object_collect_values

except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args

#metodo que recebe o json que contem regras de contigencia
class EngineRule(object):
    """docstring for EngineRule"""

    core_father = None
    def __init__(self, parent):             #instância do objeto e inicia o escalonador
        self.uuid = None
        self.core = parent

    def get_rules(self,uuid): # método encarrgado de extrair a regra do bd por meio de API restfull e retorna um json da regra

        param     = {"uuID":uuid}
        getSensor = self.core.API_access("get", "sensors", model_id=None, data=None, param=param).json()
        id_sensor =  getSensor[0]['id']

        self.id_sensor = getSensor[0]['uuID']

        param     = {"sensor":id_sensor}
        rules     = self.core.API_access("get", "rules", model_id=None, data=None, param=param).json()
        return rules

    def get_parameters(self,obj_json): # pega os parametros enviados pelo tratador de evento e retorna um disct destes parametros

        parameters = json.loads(obj_json)
        return parameters


    def run_rules(self,parameters_of_gateway): # executa a regra

        parameters     = self.get_parameters(parameters_of_gateway)
        obj_parameters = Parameters() #

        rules = self.get_rules(parameters['id'])
        for i in range(0,len(rules),1): # percorre a lista que contem as regras

            if(rules[i]['status']):
                rule = json.loads(rules[i]['jsonRule']) # extrai as regras do json
                condiction_satisfied = run_all(rule_list=rule,
                defined_variables=ConditionsRules(obj_parameters,self.core),
                defined_actions=ActionRules(obj_parameters,self.core),
                stop_on_first_trigger=True
                )
                '''De interesse do povo da fog
                    envio  de dado o id da regra, a data de execução (com delay) da regra e um atributo informando
                    se as condições foram satisfeitas ou não.
                   topic (topico), ip_edge_receive (ip destino) devem ser implementados'''
                date_now        = datetime.datetime.now()
                date_str        = date_now.strftime("%Y-%m-%d %H:%M:%S")
                topic           = None#self.core.API_access("get", "sensors", model_id=None, data=None, param=param).json()
                ip_edge_receive = None#self.core.API_access("get", "sensors", model_id=None, data=None, param=param).json()
                pay_load        = {}
                pay_load['condiction_satisfied'] = condiction_satisfied
                pay_load['id_rule']              = rules[i]['id']
                pay_load['rule']                 = rules[i]['jsonRule']
                pay_load['date']                 = date_str
                pay_load['value_sensor']         = self.get_value_sensor()
                pay_load['uuID']                 = self.uuid_sensor
                mqtt_broker                      = Publish()
                mqtt_broker.send_message(topic,json.dumps(pay_load),ip_edge_receive)


    def run_rules_event(self,datas_of_rules): # atributos do datas_of_rules: id da regra que gerou o evento, o status de execução, o valor de sensor, a regra a ser executada

        data_received_of_broker = json.loads(datas_of_rules)

        obj_parameters = Parameters(datas_of_rules) #gera os parametros para executar a regra
        rules          = self.get_rules(datas_of_rules)
        obj_parameters = Parameters() #aqui vai passar o true/false da regra que gerou o evento

        for i in range(0,len(rules),1): # percorre a lista que contem as regras
            if(rules[i]['status']):
                rule  = json.loads(rules[i]['jsonRule']) # extrai as regras do json
                run_all(rule_list=rule,
                    defined_variables=ConditionsRules(obj_parameters,self.core),
                    defined_actions=ActionRules(obj_parameters,self.core),
                    stop_on_first_trigger=True
                )
    def get_value_sensor(self):
        # realiza a coleta do sensor

            collect_data['uuID']            = self.uuid_sensor
            collect_data['event']           = "gathering"
            collect_data['collect_to_rule'] = True

            param        = {"uuID":collect_data['uuID']}
            info_gateway = self.core_father.API_access("get", "sensors", model_id=None, data=None, param=param).json()

            id_gateway              = info_gateway[0]['gateway']
            collect_data['gateway'] = id_gateway
            json_dumps_collect_data = collect_data

            object_events           = object_collect_values.event_treatment.Event_Treatment(self.core_father)
            info_gateway_and_sensor = object_events.event(json_dumps_collect_data)# tratar erro de comunicação, gateway e/ou sensor

         #finaliza a a coleta do sensor.
            return float(info_gateway_and_sensor['value'])

from core.publisher_mqtt import *
from core.gathering import Gathering
