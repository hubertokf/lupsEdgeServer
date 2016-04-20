# Em teste
from business_rules import run_all
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC, FIELD_TEXT
from ActionRules import ActionRules
from ConditionsRules import ConditionsRules
import simplejson
import os
#metodo que recebe o json que contm regras de contigencia
def get_rules(a):

    with open ('ru.json') as f:
        rules = simplejson.load(f)
    return rules

#def trigger_ruler():
if __name__ == "__main__":
    from business_rules import export_rule_data
    #export_rule_data(Num, Actions)
    rules = get_rules("ok")
    run_all(rule_list=rules,
            defined_variables=ConditionsRules(3),
            defined_actions=ActionRules(),
            stop_on_first_trigger=True
           )
