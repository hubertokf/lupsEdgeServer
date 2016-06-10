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


    @rule_action(params={"info_adicional":FIELD_NUMERIC })
    def publish(self,info_adicional):
        json = '{"id_sensor: {0}, "event": "{1}", "valor",{2}}'.format(self.parameters.id,self.parameters.event,self.parameters.value)
        #chamar tratador de evento

    @rule_action(params={"info_adicional":FIELD_NUMERIC })
    def gathering(self,info_adicional):
        json = '{"id_sensor: {0}, "event": "{1}", "valor",{2}}'.format(self.parameters.id,self.parameters.event,self.parameters.value)
        #chamar tratador de evento

    @rule_action(params={"info_adicional":FIELD_NUMERIC })
    def proceding(self,info_adicional):
        json = '{"id_sensor: {0}, "event": "{1}", "valor",{2}}'.format(self.parameters.id,self.parameters.event,self.parameters.value)
        #chamar tratador de evento

    @rule_action(params = {"inf": FIELD_TEXT})
    def test_post_Event(self, inf):
        params_event = self.parameters.event
        params_id = self.parameters.id
        decoJson = {'event' : params_event,
                    'id' : params_id}
        coJson = json.dumps(decoJson)
        print(inf)
