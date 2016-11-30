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

    def get_rules(self,a): # método encarrgado de extrair a regra do bd por meio de APU restfull e retorna um json da regra


        # headers   = {'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"}
        # url       = 'http://localhost:8000/sensors/?format=json&uuID={0}'.format(a)
        # r         = requests.get(url, headers=headers)
        # getSensor = r.json()

        param = {"uuID":a}
        getSensor = self.core.API_access("get", "sensors", model_id=None, data=None, param=param).json()
         
        id_sensor =  getSensor[0]['id']
        print(id_sensor)

        # url       = 'http://localhost:8000/rules/?format=json&sensor={0}'.format(id_sensor)
        # r         = requests.get(url, headers=headers)
        # rules     = r.json() # coleta os dados recebidos da APIrestfull

        param = {"sensor":id_sensor}
        rules = self.core.API_access("get", "rules", model_id=None, data=None, param=param).json()


        return rules

    def get_parameters(self,obj_json): # pega os parametros enviados pelo tratador de evento e retorna um disct destes parametros
        # print(obj_json)
        parameters = json.loads(obj_json)
        # print(type(parameters))
        return parameters
        #return parameters


    def run_rules(self,a): # executa a regra
        parameters = self.get_parameters(a)
        # obj_parameters= Parameters(parameters['id'],parameters['valor'],parameters['id_gateway']) #id_gateway futuramente será trabalhado
        obj_parameters= Parameters() #id_gateway futuramente será trabalhado

        rules = self.get_rules(parameters['id'])
        for i in range(0,len(rules),1): # percorre a lista que contem as regras
            #print(type(rules[i]['status']))
            if(rules[i]['status']):
                rule = json.loads(rules[i]['jsonRule']) # extrai as regras do json
                run_all(rule_list=rule,

                defined_variables=ConditionsRules(obj_parameters,self.core),
                defined_actions=ActionRules(obj_parameters,self.core),
                stop_on_first_trigger=True
                )

    def run_rules_t(self,a): # executa a regra

        obj_parameters= Parameters(10,30,10) #id_gateway futuramente será trabalhado
        rules = self.get_rules(a)
        #print("aioeuoaieuaeioea")
        for i in range(0,len(rules),1): # percorre a lista que contem as regras
            #print(i)
            if(rules[i]['status']):
                rule = json.loads(rules[i]['jsonRule']) # extrai as regras do json
                run_all(rule_list=rule,

                defined_variables=ConditionsRules(obj_parameters,self.core),
                defined_actions=ActionRules(obj_parameters,self.core),
                stop_on_first_trigger=True
                )
