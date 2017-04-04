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
    import json
    import os
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args

#metodo que recebe o json que contem regras de contigencia
class EngineRule(object):
    """docstring for EngineRule"""
    core = None

    def __init__(self, parent):             #instância do objeto e inicia o escalonador

        self.core = parent

    def get_rules(self,uuid): # método encarrgado de extrair a regra do bd por meio de API restfull e retorna um json da regra

        param     = {"uuID":uuid}
        getSensor = self.core.API_access("get", "sensors", model_id=None, data=None, param=param).json()
        id_sensor =  getSensor[0]['id']

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
                run_all(rule_list=rule,
                defined_variables=ConditionsRules(obj_parameters,self.core),
                defined_actions=ActionRules(obj_parameters,self.core),
                stop_on_first_trigger=True
                )

    def run_rules_event(self,datas_of_rules): # atributos do datas_of_rules: id da regra que gerou o evento, o status de execução, o valor de sensor, a regra a ser executada

        obj_parameters = Parameters(datas_of_rules) #gera os parametros para executar a regra
        rules          = self.get_rules(datas_of_rules)
        obj_parameters = Parameters() #aqui vai passar o true/false da regra que gerou o evento
        for i in range(0,len(rules),1): # percorre a lista que contem as regras
            if(rules[i]['status']):
            rule = json.loads(rules[i]['jsonRule']) # extrai as regras do json
            run_all(rule_list=rule,
                    defined_variables=ConditionsRules(obj_parameters,self.core),
                    defined_actions=ActionRules(obj_parameters,self.core),
                    stop_on_first_trigger=True
                )
