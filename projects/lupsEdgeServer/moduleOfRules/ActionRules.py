from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC, FIELD_TEXT

class ActionRules(BaseActions):

    def __init__ (self, parameters):
        self.parameters = parameters

    @rule_action(params={"teste": FIELD_TEXT})
    def atuar(self,teste):
        print(teste)
    # método para atuação (evento atuar)

    @rule_action(params={"test":FIELD_NUMERIC })
    def string_action(self,test):
        print (self.parameters.event,self.parameters.id,self.parameters.value)
