from business_rules.variables import BaseVariables, numeric_rule_variable

class ConditionsRules(BaseVariables):
    def __init__ (self, parameters):
        self.parameters = parameters

    @numeric_rule_variable
    def getNumber(self):
        return self.parameters.value

    @numeric_rule_variable
    def getContador(self):
        return self.parameters.contador
