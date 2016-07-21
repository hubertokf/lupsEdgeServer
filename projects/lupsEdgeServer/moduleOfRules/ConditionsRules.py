from business_rules.variables import BaseVariables, numeric_rule_variable
from moduleOfRules.EngineRuleEdge import EngineRule
class ConditionsRules(BaseVariables):
    def __init__ (self, parameters):
        self.parameters = parameters

    @numeric_rule_variable
    def getNumber(self):
        return self.parameters.value

    @boolean_rule_variable
    def fault_check_x(self):

        total_verificacao = 10
        contador = total_verificacao
        engine = new EngineRule()
        trigger = False
        ruler = self.ruler()

        while (contador > 0 && trigger == False):

                '''Instaciar objeto gathering'''
                string = "{{"id": {0}, "event" : {1}, "value" : {2}}}".format(18,"e",105)
                trigger = engine.run_rules_error(ruler,string)
                contador = contador - 1

        return trigger

    def ruler():
        rule =
        """[{"conditions":{"all":[{"name":getNumber,"operator":"less_than","value":99.9}]}},{"actions":"none","params": {"inf":}}]"""

    return rule
