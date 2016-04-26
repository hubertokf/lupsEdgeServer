# Em teste
from business_rules import run_all
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC, FIELD_TEXT
from ActionRules import ActionRules
from ConditionsRules import ConditionsRules
from Parameters import Parameters
import simplejson
import os
#metodo que recebe o json que contem regras de contigencia
def get_rules(a):

    with open ('ru.json') as f:
        rules = simplejson.load(f)
    return rules

def get_parameters(json):

    with open (json) as f:
        parameters = simplejson.load(f)
    return parameters

def trigger_ruler():
    # aqui deve inserir a busca da regra no BD a partir do id do sensor
    get_rules(files)

if __name__ == "__main__":

    parameters = get_parameters("teste/testeparameters.json")
    obj_parameters= Parameters(parameters['evento'],parameters['id'],parameters['valor'])
    rules = get_rules("ok")

    run_all(rule_list=rules,
            defined_variables=ConditionsRules(3),
            defined_actions=ActionRules(obj_parameters),
            stop_on_first_trigger=True
           )
