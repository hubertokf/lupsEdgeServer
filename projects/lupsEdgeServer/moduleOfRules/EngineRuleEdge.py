# Em teste
from business_rules import run_all
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC, FIELD_TEXT
from ActionRules import ActionRules
from ConditionsRules import ConditionsRules
from Parameters import Parameters
import requests
import json
import os
#metodo que recebe o json que contem regras de contigencia
class EngineRule(object):
    """docstring for EngineRule"""


    def get_rules(self,a): # método encarrgado de extrair a regra do bd por meio de APU restfull e retorna um json da regra


        headers = {'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"}
        r = requests.get('http://localhost:8000/rules/2/?format=json', headers=headers)

        rules = r.json() # coleta os dados recebidos da APIrestfull
        rules = json.loads(rules['jsonRule']) # transforma json em dist
        return rules

    def get_parameters(self,obj_json): # pega os parametros enviados pelo tratador de evento e retorna um disct destes parametros

        parameters = json.loads(obj_json)
        return parameters


    def run_rules(self,a): # executa a regra

        parameters = self.get_parameters(a)
        obj_parameters= Parameters(parameters['evento'],parameters['id'],parameters['valor'])
        rules = self.get_rules(parameters['id'])

        run_all(rule_list=rules,
                defined_variables=ConditionsRules(parameters['valor']),
                defined_actions=ActionRules(obj_parameters),
                stop_on_first_trigger=True
            )
