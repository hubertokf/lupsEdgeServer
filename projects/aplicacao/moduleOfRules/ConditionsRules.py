from business_rules.variables import BaseVariables, numeric_rule_variable

class ConditionsRules(BaseVariables):
    def __init__ (self, number):
        self.number = number

    @numeric_rule_variable
    def getNumber(self): 
        return self.number
