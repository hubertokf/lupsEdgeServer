from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC, FIELD_TEXT
import json
from business_rules import run_all
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC, FIELD_TEXT
from ConditionsRules import ConditionsRules
from Parameters import Parameters
import os

class ActionRules(BaseActions):

    def __init__ (self, parameters):
        self.parameters = parameters

    @rule_action(params={"teste": FIELD_TEXT})
    def atuar(self,teste):
            print("ok")

    @rule_action(params={"test":FIELD_NUMERIC })
    def string_action(self,test):
        print (self.parameters.event,self.parameters.id,self.parameters.value)

    @rule_action(params = {"inf": FIELD_TEXT})
    def test_post_Event(self, inf):
        params_event = self.parameters.event
        params_id = self.parameters.id
        decoJson = {'event' : params_event,
                    'id' : params_id}
        coJson = json.dumps(decoJson)
        print(inf)
